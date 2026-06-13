"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FixedUpfrontPricingTerm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.currency_code
    import aws_sdk_marketplace_agreement.types.grant_list
    import aws_sdk_marketplace_agreement.types.term_id
    import aws_sdk_marketplace_agreement.types.unversioned_term_type


class FixedUpfrontPricingTerm(TypedDict):
    type: NotRequired[
        "aws_sdk_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term being updated.</p>"""
    id: NotRequired["aws_sdk_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    currency_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>Defines the currency for the prices mentioned in this term. </p>"""
    duration: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Contract duration for the terms.</p>"""
    price: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Fixed amount to be charged to the customer when this term is accepted.</p>"""
    grants: NotRequired["aws_sdk_marketplace_agreement.types.grant_list.GrantList"]
    """<p>Entitlements granted to the acceptor of fixed upfront as part of agreement execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FixedUpfrontPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "price" in value:
        out["price"] = value["price"]
    if "grants" in value:
        import aws_sdk_marketplace_agreement.types.grant_list

        out["grants"] = (
            aws_sdk_marketplace_agreement.types.grant_list.serialize_aws_json_1_0(
                value["grants"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FixedUpfrontPricingTerm:
    out: FixedUpfrontPricingTerm = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "id" in data:
        out["id"] = data["id"]
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "price" in data:
        out["price"] = data["price"]
    if "grants" in data:
        import aws_sdk_marketplace_agreement.types.grant_list

        out["grants"] = (
            aws_sdk_marketplace_agreement.types.grant_list.deserialize_aws_json_1_0(
                data["grants"]
            )
        )
    return out
