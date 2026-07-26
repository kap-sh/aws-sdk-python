"""Generated from Smithy shape ``com.amazonaws.guardduty#Criterion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.condition
    import capo_guardduty.types.string

Criterion: TypeAlias = dict[
    "capo_guardduty.types.string.String", "capo_guardduty.types.condition.Condition"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Criterion) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_guardduty.types.condition

        out[key] = capo_guardduty.types.condition.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Criterion:
    out: Criterion = {}
    for key, value in data.items():
        import capo_guardduty.types.condition

        out[key] = capo_guardduty.types.condition.deserialize_json(value)
    return out
