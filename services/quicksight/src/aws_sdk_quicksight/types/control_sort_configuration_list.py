"""Generated from Smithy shape ``com.amazonaws.quicksight#ControlSortConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.control_sort_configuration

ControlSortConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.control_sort_configuration.ControlSortConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlSortConfigurationList) -> list:
    import aws_sdk_quicksight.types.control_sort_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.control_sort_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ControlSortConfigurationList:
    import aws_sdk_quicksight.types.control_sort_configuration

    out: ControlSortConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.control_sort_configuration.deserialize_json(item)
        )
    return out
