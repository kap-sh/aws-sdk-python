"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#InvoicingEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string


class InvoicingEntity(TypedDict, closed=True):
    legal_name: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Legal name of the entity issuing the invoice.</p>"""
    branch_name: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The branch where the issuing entity is operating from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoicingEntity) -> dict:
    out: dict = {}
    if "legal_name" in value:
        out["legalName"] = value["legal_name"]
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoicingEntity:
    out: InvoicingEntity = {}  # type: ignore[typeddict-item]
    if "legalName" in data:
        out["legal_name"] = data["legalName"]
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    return out
