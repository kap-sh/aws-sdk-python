"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Button``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.button_text
    import aws_sdk_lex_runtime_v2.types.button_value


class Button(TypedDict):
    text: "aws_sdk_lex_runtime_v2.types.button_text.ButtonText"
    """<p>The text that is displayed on the button.</p>"""
    value: "aws_sdk_lex_runtime_v2.types.button_value.ButtonValue"
    """<p>The value returned to Amazon Lex V2 when a user chooses the button.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Button) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Button:
    out: Button = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("Button.text required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Button.value required")
    return out
