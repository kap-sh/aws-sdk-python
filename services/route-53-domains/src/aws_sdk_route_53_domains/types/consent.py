"""Generated from Smithy shape ``com.amazonaws.route53domains#Consent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.currency
    import aws_sdk_route_53_domains.types.price


class Consent(TypedDict):
    max_price: "aws_sdk_route_53_domains.types.price.Price"
    """<p> Maximum amount the customer agreed to accept. </p>"""
    currency: "aws_sdk_route_53_domains.types.currency.Currency"
    """<p> Currency for the <code>MaxPrice</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Consent) -> dict:
    out: dict = {}
    out["MaxPrice"] = value.get("max_price", 0)
    out["Currency"] = value["currency"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Consent:
    out: Consent = {}  # type: ignore[typeddict-item]
    if "MaxPrice" in data:
        out["max_price"] = data["MaxPrice"]
    else:
        out["max_price"] = 0
    if "Currency" in data:
        out["currency"] = data["Currency"]
    else:
        raise DeserializationError("Consent.currency required")
    return out
