"""Generated from Smithy shape ``com.amazonaws.chime#UpdateBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.nullable_boolean


class UpdateBotRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The bot ID.</p>"""
    disabled: NotRequired["aws_sdk_chime.types.nullable_boolean.NullableBoolean"]
    """<p>When true, stops the specified bot from running in your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotRequest) -> dict:
    out: dict = {}
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    return out


def deserialize_json(data: dict) -> UpdateBotRequest:
    out: UpdateBotRequest = {}  # type: ignore[typeddict-item]
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    return out
