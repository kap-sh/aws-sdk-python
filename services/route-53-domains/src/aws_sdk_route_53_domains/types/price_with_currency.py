"""Generated from Smithy shape ``com.amazonaws.route53domains#PriceWithCurrency``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.currency
    import aws_sdk_route_53_domains.types.price


class PriceWithCurrency(TypedDict, closed=True):
    price: "aws_sdk_route_53_domains.types.price.Price"
    """<p>The price of a domain, in a specific currency.</p>"""
    currency: "aws_sdk_route_53_domains.types.currency.Currency"
    """<p>The currency specifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriceWithCurrency) -> dict:
    out: dict = {}
    out["Price"] = value.get("price", 0)
    out["Currency"] = value["currency"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PriceWithCurrency:
    out: PriceWithCurrency = {}  # type: ignore[typeddict-item]
    if "Price" in data:
        out["price"] = data["Price"]
    else:
        out["price"] = 0
    if "Currency" in data:
        out["currency"] = data["Currency"]
    else:
        raise DeserializationError("PriceWithCurrency.currency required")
    return out
