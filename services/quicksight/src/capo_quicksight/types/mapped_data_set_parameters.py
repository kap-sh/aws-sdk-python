"""Generated from Smithy shape ``com.amazonaws.quicksight#MappedDataSetParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.mapped_data_set_parameter

MappedDataSetParameters: TypeAlias = list[
    "capo_quicksight.types.mapped_data_set_parameter.MappedDataSetParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: MappedDataSetParameters) -> list:
    import capo_quicksight.types.mapped_data_set_parameter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.mapped_data_set_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> MappedDataSetParameters:
    import capo_quicksight.types.mapped_data_set_parameter

    out: MappedDataSetParameters = []
    for item in data:
        out.append(
            capo_quicksight.types.mapped_data_set_parameter.deserialize_json(item)
        )
    return out
