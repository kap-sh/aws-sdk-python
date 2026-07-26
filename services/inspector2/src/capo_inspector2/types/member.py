"""Generated from Smithy shape ``com.amazonaws.inspector2#Member``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.relationship_status


class Member(TypedDict, closed=True):
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the member account.</p>"""
    relationship_status: NotRequired[
        "capo_inspector2.types.relationship_status.RelationshipStatus"
    ]
    """<p>The status of the member account.</p>"""
    delegated_admin_account_id: NotRequired[
        "capo_inspector2.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the Amazon Inspector delegated administrator for this member account.</p>"""
    updated_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>A timestamp showing when the status of this member was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "relationship_status" in value:
        out["relationshipStatus"] = value["relationship_status"]
    if "delegated_admin_account_id" in value:
        out["delegatedAdminAccountId"] = value["delegated_admin_account_id"]
    if "updated_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["updatedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "relationshipStatus" in data:
        out["relationship_status"] = data["relationshipStatus"]
    if "delegatedAdminAccountId" in data:
        out["delegated_admin_account_id"] = data["delegatedAdminAccountId"]
    if "updatedAt" in data:
        import capo_inspector2.types.date_time_timestamp

        out["updated_at"] = capo_inspector2.types.date_time_timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
