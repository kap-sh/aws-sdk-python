"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SupportTerm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.term_id
    import aws_sdk_marketplace_agreement.types.unversioned_term_type


class SupportTerm(TypedDict):
    type: NotRequired[
        "aws_sdk_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term being updated.</p>"""
    id: NotRequired["aws_sdk_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    refund_policy: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Free-text field about the refund policy description that will be shown to customers as is on the website and console.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "refund_policy" in value:
        out["refundPolicy"] = value["refund_policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SupportTerm:
    out: SupportTerm = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "id" in data:
        out["id"] = data["id"]
    if "refundPolicy" in data:
        out["refund_policy"] = data["refundPolicy"]
    return out
