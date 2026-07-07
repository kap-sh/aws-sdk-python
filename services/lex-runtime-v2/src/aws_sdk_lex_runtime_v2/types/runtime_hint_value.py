"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RuntimeHintValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.runtime_hint_phrase


class RuntimeHintValue(TypedDict, closed=True):
    phrase: "aws_sdk_lex_runtime_v2.types.runtime_hint_phrase.RuntimeHintPhrase"
    """<p>The phrase that Amazon Lex V2 should look for in the user's input to the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeHintValue) -> dict:
    out: dict = {}
    out["phrase"] = value["phrase"]
    return out


def deserialize_json(data: dict) -> RuntimeHintValue:
    out: RuntimeHintValue = {}  # type: ignore[typeddict-item]
    if "phrase" in data:
        out["phrase"] = data["phrase"]
    else:
        raise DeserializationError("RuntimeHintValue.phrase required")
    return out
