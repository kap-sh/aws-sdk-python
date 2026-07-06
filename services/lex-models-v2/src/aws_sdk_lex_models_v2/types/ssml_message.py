"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SSMLMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.ssml_message_value


class SSMLMessage(TypedDict, closed=True):
    value: "aws_sdk_lex_models_v2.types.ssml_message_value.SSMLMessageValue"
    """<p>The SSML text that defines the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SSMLMessage) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SSMLMessage:
    out: SSMLMessage = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SSMLMessage.value required")
    return out
