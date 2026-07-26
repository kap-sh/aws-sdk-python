"""Generated from Smithy shape ``com.amazonaws.networkmanager#ReasonContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.reason_context_key
    import capo_networkmanager.types.reason_context_value

ReasonContextMap: TypeAlias = dict[
    "capo_networkmanager.types.reason_context_key.ReasonContextKey",
    "capo_networkmanager.types.reason_context_value.ReasonContextValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ReasonContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ReasonContextMap:
    out: ReasonContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
