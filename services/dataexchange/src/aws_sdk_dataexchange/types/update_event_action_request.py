"""Generated from Smithy shape ``com.amazonaws.dataexchange#UpdateEventActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.action


class UpdateEventActionRequest(TypedDict, closed=True):
    action: NotRequired["aws_sdk_dataexchange.types.action.Action"]
    """<p>What occurs after a certain event.</p>"""
    event_action_id: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The unique identifier for the event action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventActionRequest) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_dataexchange.types.action

        out["Action"] = aws_sdk_dataexchange.types.action.serialize_json(
            value["action"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEventActionRequest:
    out: UpdateEventActionRequest = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_dataexchange.types.action

        out["action"] = aws_sdk_dataexchange.types.action.deserialize_json(
            data["Action"]
        )
    return out
