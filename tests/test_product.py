import unittest
from pydantic import BaseModel, ValidationError, field_validator
from datetime import datetime
from typing import Optional, List, Dict, Literal, Union, Any
from checkdigit import isbn, gs1
from em_product.product import StandardProduct


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product_data = {
            "sku": "SKU123",
            "price": 10.0,
            "available_qty": 5,
            "date": "2024-09-06T10:35:27",
            "url": "https://example.com/product",
            "source": "example_source",
            "images": "https://example.com/image.jpg;https://example.com/image2.jpg",
            "product_id": "12345",
            "existence": True,
            "title": "Test Product",
            "title_en": "Test Product EN",
            "description": "This is a test product",
            "description_en": "This is an English description",
            "summary": "A short summary",
            "upc": "123456789012",
            "brand": "TestBrand",
            "specifications": [{"name": "Color", "value": "Red"}],
            "categories": "Category1>Category2",
            "videos": "https://example.com/video.mp4",
            "options": [{"name": "Color", "id": "color_1"}],
            "variants": [
                {
                    "images": "https://example.com/image.jpg;https://example.com/image2.jpg",
                    "sku": "VARIANT123",
                    "barcode": "VARIANT123",
                    "variant_id": "VARIANT123",
                    "price": 12.5,
                    "available_qty": 10,
                    "option_values": [
                        {
                            "option_id": "1",
                            "option_value_id": "10",
                            "option_name": "Size",
                            "option_value": "Medium",
                        }
                    ],
                }
            ],
            "returnable": True,
            "reviews": 100,
            "rating": 4.5,
            "sold_count": 50,
            "shipping_fee": 5.0,
            "shipping_days_min": 2,
            "shipping_days_max": 5,
            "weight": 1.2,
            "width": 10.0,
            "height": 20.0,
            "length": 15.0,
            "has_only_default_variant": False,
            "currency": "USD",
        }

    def tearDown(self):
        pass

    def test_standard_product_valid_data(self):
        StandardProduct(**self.product_data)

    def test_remove_invalid_upc(self):
        product_data = {**self.product_data, "upc": "97673485"}
        standard_product = StandardProduct(**product_data)
        self.assertIsNone(standard_product.upc)

    def test_unique_category(self):
        product_data = {**self.product_data, "categories": "Category1 > Category1"}
        with self.assertRaises(ValidationError) as context:
            StandardProduct(**product_data)

        self.assertIn("category must be unique", str(context.exception))

    def test_weight_over_limit_raises_error(self):
        product_data = {**self.product_data, "weight": 2.6}
        with self.assertRaises(ValidationError) as context:
            StandardProduct(**product_data)

        self.assertIn("weight must be less than or equal to 2.5lb", str(context.exception))


if __name__ == "__main__":
    unittest.main()
