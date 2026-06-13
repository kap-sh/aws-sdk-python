"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FreeTrialPricingTerm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.grant_list
    import aws_sdk_marketplace_agreement.types.term_id
    import aws_sdk_marketplace_agreement.types.unversioned_term_type


class FreeTrialPricingTerm(TypedDict):
    type: NotRequired[
        "aws_sdk_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term.</p>"""
    id: NotRequired["aws_sdk_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the terms.</p>"""
    duration: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Duration of the free trial period (5–31 days). </p>"""
    grants: NotRequired["aws_sdk_marketplace_agreement.types.grant_list.GrantList"]
    """<p>Entitlements granted to the acceptor of a free trial as part of an agreement execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FreeTrialPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "grants" in value:
        import aws_sdk_marketplace_agreement.types.grant_list

        out["grants"] = (
            aws_sdk_marketplace_agreement.types.grant_list.serialize_aws_json_1_0(
                value["grants"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FreeTrialPricingTerm:
    out: FreeTrialPricingTerm = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "id" in data:
        out["id"] = data["id"]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "grants" in data:
        import aws_sdk_marketplace_agreement.types.grant_list

        out["grants"] = (
            aws_sdk_marketplace_agreement.types.grant_list.deserialize_aws_json_1_0(
                data["grants"]
            )
        )
    return out
