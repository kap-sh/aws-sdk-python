"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.non_empty_string


class SlotValue(TypedDict):
    interpreted_value: NotRequired[
        "aws_sdk_lex_models_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the <code>resolvedValues</code> list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotValue) -> dict:
    out: dict = {}
    if "interpreted_value" in value:
        out["interpretedValue"] = value["interpreted_value"]
    return out


def deserialize_json(data: dict) -> SlotValue:
    out: SlotValue = {}  # type: ignore[typeddict-item]
    if "interpretedValue" in data:
        out["interpreted_value"] = data["interpretedValue"]
    return out
