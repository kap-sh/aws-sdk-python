"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SampleValue``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.value


class SampleValue(TypedDict):
    value: "aws_sdk_lex_models_v2.types.value.Value"
    """<p>The value that can be used for a slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SampleValue:
    out: SampleValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SampleValue.value required")
    return out
