"""Generated from Smithy shape ``com.amazonaws.guardduty#AffectedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

AffectedResources: TypeAlias = dict[
    "capo_guardduty.types.string.String", "capo_guardduty.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AffectedResources) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AffectedResources:
    out: AffectedResources = {}
    for key, value in data.items():
        out[key] = value
    return out
