"""Generated from Smithy shape ``com.amazonaws.lakeformation#AdditionalContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.context_key
    import capo_lakeformation.types.context_value

AdditionalContextMap: TypeAlias = dict[
    "capo_lakeformation.types.context_key.ContextKey",
    "capo_lakeformation.types.context_value.ContextValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdditionalContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AdditionalContextMap:
    out: AdditionalContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
