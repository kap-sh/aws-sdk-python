"""Generated from Smithy shape ``com.amazonaws.quicksight#MappedDataSetParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.mapped_data_set_parameter

MappedDataSetParameters: TypeAlias = list[
    "aws_sdk_quicksight.types.mapped_data_set_parameter.MappedDataSetParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: MappedDataSetParameters) -> list:
    import aws_sdk_quicksight.types.mapped_data_set_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.mapped_data_set_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MappedDataSetParameters:
    import aws_sdk_quicksight.types.mapped_data_set_parameter

    out: MappedDataSetParameters = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.mapped_data_set_parameter.deserialize_json(item)
        )
    return out
