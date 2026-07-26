"""Generated from Smithy shape ``com.amazonaws.databrew#ColumnStatisticsConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.column_statistics_configuration

ColumnStatisticsConfigurationList: TypeAlias = list[
    "capo_databrew.types.column_statistics_configuration.ColumnStatisticsConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnStatisticsConfigurationList) -> list:
    import capo_databrew.types.column_statistics_configuration

    out: list = []
    for item in value:
        out.append(
            capo_databrew.types.column_statistics_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ColumnStatisticsConfigurationList:
    import capo_databrew.types.column_statistics_configuration

    out: ColumnStatisticsConfigurationList = []
    for item in data:
        out.append(
            capo_databrew.types.column_statistics_configuration.deserialize_json(item)
        )
    return out
