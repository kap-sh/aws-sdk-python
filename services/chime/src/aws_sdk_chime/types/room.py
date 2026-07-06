"""Generated from Smithy shape ``com.amazonaws.chime#Room``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.iso8601_timestamp
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.sensitive_string


class Room(TypedDict, closed=True):
    room_id: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The room ID.</p>"""
    name: NotRequired["aws_sdk_chime.types.sensitive_string.SensitiveString"]
    """<p>The room name.</p>"""
    account_id: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Chime account ID.</p>"""
    created_by: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the room creator.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The room creation timestamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The room update timestamp, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Room) -> dict:
    out: dict = {}
    if "room_id" in value:
        out["RoomId"] = value["room_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "created_timestamp" in value:
        import aws_sdk_chime.types.iso8601_timestamp

        out["CreatedTimestamp"] = aws_sdk_chime.types.iso8601_timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime.types.iso8601_timestamp

        out["UpdatedTimestamp"] = aws_sdk_chime.types.iso8601_timestamp.serialize_json(
            value["updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> Room:
    out: Room = {}  # type: ignore[typeddict-item]
    if "RoomId" in data:
        out["room_id"] = data["RoomId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "CreatedTimestamp" in data:
        import aws_sdk_chime.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    return out
