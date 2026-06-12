"""Generated from Smithy shape ``com.amazonaws.databrew#ColumnStatisticsConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.column_statistics_configuration

ColumnStatisticsConfigurationList: TypeAlias = list[
    "aws_sdk_databrew.types.column_statistics_configuration.ColumnStatisticsConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnStatisticsConfigurationList) -> list:
    import aws_sdk_databrew.types.column_statistics_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_databrew.types.column_statistics_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ColumnStatisticsConfigurationList:
    import aws_sdk_databrew.types.column_statistics_configuration

    out: ColumnStatisticsConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_databrew.types.column_statistics_configuration.deserialize_json(
                item
            )
        )
    return out
