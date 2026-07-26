"""Generated from Smithy shape ``com.amazonaws.guardduty#CountBySeverity``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.string

CountBySeverity: TypeAlias = dict[
    "capo_guardduty.types.string.String", "capo_guardduty.types.integer.Integer"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CountBySeverity) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CountBySeverity:
    out: CountBySeverity = {}
    for key, value in data.items():
        out[key] = value
    return out
