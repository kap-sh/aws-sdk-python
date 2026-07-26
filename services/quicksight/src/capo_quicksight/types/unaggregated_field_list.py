"""Generated from Smithy shape ``com.amazonaws.quicksight#UnaggregatedFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.unaggregated_field

UnaggregatedFieldList: TypeAlias = list[
    "capo_quicksight.types.unaggregated_field.UnaggregatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnaggregatedFieldList) -> list:
    import capo_quicksight.types.unaggregated_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.unaggregated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnaggregatedFieldList:
    import capo_quicksight.types.unaggregated_field

    out: UnaggregatedFieldList = []
    for item in data:
        out.append(capo_quicksight.types.unaggregated_field.deserialize_json(item))
    return out
