"""Generated from Smithy shape ``com.amazonaws.chatbot#GetCustomActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.custom_action_arn


class GetCustomActionRequest(TypedDict, closed=True):
    custom_action_arn: "aws_sdk_chatbot.types.custom_action_arn.CustomActionArn"
    """<p>Returns the fully defined Amazon Resource Name (ARN) of the custom action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomActionRequest) -> dict:
    out: dict = {}
    out["CustomActionArn"] = value["custom_action_arn"]
    return out


def deserialize_json(data: dict) -> GetCustomActionRequest:
    out: GetCustomActionRequest = {}  # type: ignore[typeddict-item]
    if "CustomActionArn" in data:
        out["custom_action_arn"] = data["CustomActionArn"]
    else:
        raise DeserializationError("GetCustomActionRequest.custom_action_arn required")
    return out
