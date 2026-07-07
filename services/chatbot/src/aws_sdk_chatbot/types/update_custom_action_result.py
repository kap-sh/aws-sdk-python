"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateCustomActionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.custom_action_arn


class UpdateCustomActionResult(TypedDict, closed=True):
    custom_action_arn: "aws_sdk_chatbot.types.custom_action_arn.CustomActionArn"
    """<p>The fully defined ARN of the custom action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomActionResult) -> dict:
    out: dict = {}
    out["CustomActionArn"] = value["custom_action_arn"]
    return out


def deserialize_json(data: dict) -> UpdateCustomActionResult:
    out: UpdateCustomActionResult = {}  # type: ignore[typeddict-item]
    if "CustomActionArn" in data:
        out["custom_action_arn"] = data["CustomActionArn"]
    else:
        raise DeserializationError(
            "UpdateCustomActionResult.custom_action_arn required"
        )
    return out
