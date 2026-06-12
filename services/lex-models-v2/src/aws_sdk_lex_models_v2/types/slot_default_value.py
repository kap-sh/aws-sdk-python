"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotDefaultValue``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.slot_default_value_string


class SlotDefaultValue(TypedDict):
    default_value: (
        "aws_sdk_lex_models_v2.types.slot_default_value_string.SlotDefaultValueString"
    )
    """<p>The default value to use when a user doesn't provide a value for a slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotDefaultValue) -> dict:
    out: dict = {}
    out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> SlotDefaultValue:
    out: SlotDefaultValue = {}  # type: ignore[typeddict-item]
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    else:
        raise DeserializationError("SlotDefaultValue.default_value required")
    return out
