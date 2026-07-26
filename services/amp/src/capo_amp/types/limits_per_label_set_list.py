"""Generated from Smithy shape ``com.amazonaws.amp#LimitsPerLabelSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amp.types.limits_per_label_set

LimitsPerLabelSetList: TypeAlias = list[
    "capo_amp.types.limits_per_label_set.LimitsPerLabelSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: LimitsPerLabelSetList) -> list:
    import capo_amp.types.limits_per_label_set

    out: list = []
    for item in value:
        out.append(capo_amp.types.limits_per_label_set.serialize_json(item))
    return out


def deserialize_json(data: list) -> LimitsPerLabelSetList:
    import capo_amp.types.limits_per_label_set

    out: LimitsPerLabelSetList = []
    for item in data:
        out.append(capo_amp.types.limits_per_label_set.deserialize_json(item))
    return out
