"""Generated from Smithy shape ``com.amazonaws.macie2#Invitation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.relationship_status


class Invitation(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account that sent the invitation.</p>"""
    invitation_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the invitation.</p>"""
    invited_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the invitation was sent.</p>"""
    relationship_status: NotRequired[
        "aws_sdk_macie2.types.relationship_status.RelationshipStatus"
    ]
    """<p>The status of the relationship between the account that sent the invitation and the account that received the invitation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Invitation) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "invitation_id" in value:
        out["invitationId"] = value["invitation_id"]
    if "invited_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["invitedAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["invited_at"]
        )
    if "relationship_status" in value:
        import aws_sdk_macie2.types.relationship_status

        out["relationshipStatus"] = (
            aws_sdk_macie2.types.relationship_status.serialize_json(
                value["relationship_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> Invitation:
    out: Invitation = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "invitationId" in data:
        out["invitation_id"] = data["invitationId"]
    if "invitedAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["invited_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["invitedAt"]
        )
    if "relationshipStatus" in data:
        import aws_sdk_macie2.types.relationship_status

        out["relationship_status"] = (
            aws_sdk_macie2.types.relationship_status.deserialize_json(
                data["relationshipStatus"]
            )
        )
    return out
