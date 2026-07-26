"""Generated from Smithy shape ``com.amazonaws.quicksight#ControlSortConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.control_sort_configuration

ControlSortConfigurationList: TypeAlias = list[
    "capo_quicksight.types.control_sort_configuration.ControlSortConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlSortConfigurationList) -> list:
    import capo_quicksight.types.control_sort_configuration

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.control_sort_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ControlSortConfigurationList:
    import capo_quicksight.types.control_sort_configuration

    out: ControlSortConfigurationList = []
    for item in data:
        out.append(
            capo_quicksight.types.control_sort_configuration.deserialize_json(item)
        )
    return out
