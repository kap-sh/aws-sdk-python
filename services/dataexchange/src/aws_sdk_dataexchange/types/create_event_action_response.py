"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateEventActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.action
    import aws_sdk_dataexchange.types.arn
    import aws_sdk_dataexchange.types.event
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.map_of__string
    import aws_sdk_dataexchange.types.timestamp


class CreateEventActionResponse(TypedDict, closed=True):
    action: NotRequired["aws_sdk_dataexchange.types.action.Action"]
    """<p>What occurs after a certain event.</p>"""
    arn: NotRequired["aws_sdk_dataexchange.types.arn.Arn"]
    """<p>The ARN for the event action.</p>"""
    created_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the event action was created, in ISO 8601 format.</p>"""
    event: NotRequired["aws_sdk_dataexchange.types.event.Event"]
    """<p>What occurs to start an action.</p>"""
    id: NotRequired["aws_sdk_dataexchange.types.id.Id"]
    """<p>The unique identifier for the event action.</p>"""
    tags: NotRequired["aws_sdk_dataexchange.types.map_of__string.MapOf__string"]
    """<p>The tags for the event action.</p>"""
    updated_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the event action was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventActionResponse) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_dataexchange.types.action

        out["Action"] = aws_sdk_dataexchange.types.action.serialize_json(
            value["action"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["CreatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "event" in value:
        import aws_sdk_dataexchange.types.event

        out["Event"] = aws_sdk_dataexchange.types.event.serialize_json(value["event"])
    if "id" in value:
        out["Id"] = value["id"]
    if "tags" in value:
        import aws_sdk_dataexchange.types.map_of__string

        out["Tags"] = aws_sdk_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    if "updated_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["UpdatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CreateEventActionResponse:
    out: CreateEventActionResponse = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_dataexchange.types.action

        out["action"] = aws_sdk_dataexchange.types.action.deserialize_json(
            data["Action"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["created_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "Event" in data:
        import aws_sdk_dataexchange.types.event

        out["event"] = aws_sdk_dataexchange.types.event.deserialize_json(data["Event"])
    if "Id" in data:
        out["id"] = data["Id"]
    if "Tags" in data:
        import aws_sdk_dataexchange.types.map_of__string

        out["tags"] = aws_sdk_dataexchange.types.map_of__string.deserialize_json(
            data["Tags"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["updated_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
