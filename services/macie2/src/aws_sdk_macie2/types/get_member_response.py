"""Generated from Smithy shape ``com.amazonaws.macie2#GetMemberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.relationship_status
    import aws_sdk_macie2.types.tag_map


class GetMemberResponse(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account.</p>"""
    administrator_account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the administrator account.</p>"""
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the account.</p>"""
    email: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The email address for the account. This value is null if the account is associated with the administrator account through Organizations.</p>"""
    invited_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when an Amazon Macie membership invitation was last sent to the account. This value is null if a Macie membership invitation hasn't been sent to the account.</p>"""
    master_account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>(Deprecated) The Amazon Web Services account ID for the administrator account. This property has been replaced by the administratorAccountId property and is retained only for backward compatibility.</p>"""
    relationship_status: NotRequired[
        "aws_sdk_macie2.types.relationship_status.RelationshipStatus"
    ]
    """<p>The current status of the relationship between the account and the administrator account.</p>"""
    tags: NotRequired["aws_sdk_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies which tags (keys and values) are associated with the account in Amazon Macie.</p>"""
    updated_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status of the relationship between the account and the administrator account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemberResponse) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "administrator_account_id" in value:
        out["administratorAccountId"] = value["administrator_account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "email" in value:
        out["email"] = value["email"]
    if "invited_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["invitedAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["invited_at"]
        )
    if "master_account_id" in value:
        out["masterAccountId"] = value["master_account_id"]
    if "relationship_status" in value:
        import aws_sdk_macie2.types.relationship_status

        out["relationshipStatus"] = (
            aws_sdk_macie2.types.relationship_status.serialize_json(
                value["relationship_status"]
            )
        )
    if "tags" in value:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.serialize_json(value["tags"])
    if "updated_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["updatedAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetMemberResponse:
    out: GetMemberResponse = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "administratorAccountId" in data:
        out["administrator_account_id"] = data["administratorAccountId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "email" in data:
        out["email"] = data["email"]
    if "invitedAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["invited_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["invitedAt"]
        )
    if "masterAccountId" in data:
        out["master_account_id"] = data["masterAccountId"]
    if "relationshipStatus" in data:
        import aws_sdk_macie2.types.relationship_status

        out["relationship_status"] = (
            aws_sdk_macie2.types.relationship_status.deserialize_json(
                data["relationshipStatus"]
            )
        )
    if "tags" in data:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.deserialize_json(data["tags"])
    if "updatedAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["updated_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["updatedAt"]
        )
    return out
