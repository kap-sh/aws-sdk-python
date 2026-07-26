"""Generated from Smithy shape ``com.amazonaws.securityir#GetMembershipAccountDetailItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.aws_account_id
    import capo_security_ir.types.membership_account_relationship_status
    import capo_security_ir.types.membership_account_relationship_type


class GetMembershipAccountDetailItem(TypedDict, closed=True):
    account_id: NotRequired["capo_security_ir.types.aws_account_id.AWSAccountId"]
    """<p/>"""
    relationship_status: NotRequired[
        "capo_security_ir.types.membership_account_relationship_status.MembershipAccountRelationshipStatus"
    ]
    """<p/>"""
    relationship_type: NotRequired[
        "capo_security_ir.types.membership_account_relationship_type.MembershipAccountRelationshipType"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipAccountDetailItem) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "relationship_status" in value:
        import capo_security_ir.types.membership_account_relationship_status

        out["relationshipStatus"] = (
            capo_security_ir.types.membership_account_relationship_status.serialize_json(
                value["relationship_status"]
            )
        )
    if "relationship_type" in value:
        import capo_security_ir.types.membership_account_relationship_type

        out["relationshipType"] = (
            capo_security_ir.types.membership_account_relationship_type.serialize_json(
                value["relationship_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMembershipAccountDetailItem:
    out: GetMembershipAccountDetailItem = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "relationshipStatus" in data:
        import capo_security_ir.types.membership_account_relationship_status

        out["relationship_status"] = (
            capo_security_ir.types.membership_account_relationship_status.deserialize_json(
                data["relationshipStatus"]
            )
        )
    if "relationshipType" in data:
        import capo_security_ir.types.membership_account_relationship_type

        out["relationship_type"] = (
            capo_security_ir.types.membership_account_relationship_type.deserialize_json(
                data["relationshipType"]
            )
        )
    return out
