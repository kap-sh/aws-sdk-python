"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionExecutionPayloadField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_payload_field_value


class ActionExecutionPayloadField(TypedDict):
    value: "aws_sdk_qbusiness.types.action_payload_field_value.ActionPayloadFieldValue"
    """<p>The content of a user input field in an plugin action execution payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionExecutionPayloadField) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ActionExecutionPayloadField:
    out: ActionExecutionPayloadField = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("ActionExecutionPayloadField.value required")
    return out
