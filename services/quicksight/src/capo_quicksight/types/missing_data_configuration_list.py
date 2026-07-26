"""Generated from Smithy shape ``com.amazonaws.quicksight#MissingDataConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.missing_data_configuration

MissingDataConfigurationList: TypeAlias = list[
    "capo_quicksight.types.missing_data_configuration.MissingDataConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MissingDataConfigurationList) -> list:
    import capo_quicksight.types.missing_data_configuration

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.missing_data_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MissingDataConfigurationList:
    import capo_quicksight.types.missing_data_configuration

    out: MissingDataConfigurationList = []
    for item in data:
        out.append(
            capo_quicksight.types.missing_data_configuration.deserialize_json(item)
        )
    return out
