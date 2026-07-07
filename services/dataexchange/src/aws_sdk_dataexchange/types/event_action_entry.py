"""Generated from Smithy shape ``com.amazonaws.dataexchange#EventActionEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.action
    import aws_sdk_dataexchange.types.arn
    import aws_sdk_dataexchange.types.event
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.timestamp


class EventActionEntry(TypedDict, closed=True):
    action: "aws_sdk_dataexchange.types.action.Action"
    """<p>What occurs after a certain event.</p>"""
    arn: "aws_sdk_dataexchange.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the event action.</p>"""
    created_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the event action was created, in ISO 8601 format.</p>"""
    event: "aws_sdk_dataexchange.types.event.Event"
    """<p>What occurs to start an action.</p>"""
    id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the event action.</p>"""
    updated_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the event action was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventActionEntry) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.action

    out["Action"] = aws_sdk_dataexchange.types.action.serialize_json(value["action"])
    out["Arn"] = value["arn"]
    import aws_sdk_dataexchange.types.timestamp

    out["CreatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_dataexchange.types.event

    out["Event"] = aws_sdk_dataexchange.types.event.serialize_json(value["event"])
    out["Id"] = value["id"]
    import aws_sdk_dataexchange.types.timestamp

    out["UpdatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> EventActionEntry:
    out: EventActionEntry = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_dataexchange.types.action

        out["action"] = aws_sdk_dataexchange.types.action.deserialize_json(
            data["Action"]
        )
    else:
        raise DeserializationError("EventActionEntry.action required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("EventActionEntry.arn required")
    if "CreatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["created_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("EventActionEntry.created_at required")
    if "Event" in data:
        import aws_sdk_dataexchange.types.event

        out["event"] = aws_sdk_dataexchange.types.event.deserialize_json(data["Event"])
    else:
        raise DeserializationError("EventActionEntry.event required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("EventActionEntry.id required")
    if "UpdatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["updated_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("EventActionEntry.updated_at required")
    return out
