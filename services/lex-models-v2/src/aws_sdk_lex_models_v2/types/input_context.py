"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#InputContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.name


class InputContext(TypedDict, closed=True):
    name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputContext) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> InputContext:
    out: InputContext = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("InputContext.name required")
    return out
