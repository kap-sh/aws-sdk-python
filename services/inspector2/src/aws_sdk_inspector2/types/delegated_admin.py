"""Generated from Smithy shape ``com.amazonaws.inspector2#DelegatedAdmin``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.relationship_status


class DelegatedAdmin(TypedDict):
    account_id: NotRequired["aws_sdk_inspector2.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the Amazon Inspector delegated administrator for your organization.</p>"""
    relationship_status: NotRequired[
        "aws_sdk_inspector2.types.relationship_status.RelationshipStatus"
    ]
    """<p>The status of the Amazon Inspector delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DelegatedAdmin) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "relationship_status" in value:
        out["relationshipStatus"] = value["relationship_status"]
    return out


def deserialize_json(data: dict) -> DelegatedAdmin:
    out: DelegatedAdmin = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "relationshipStatus" in data:
        out["relationship_status"] = data["relationshipStatus"]
    return out
