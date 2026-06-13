"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#TemporalStatisticsListInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.temporal_statistics

TemporalStatisticsListInput: TypeAlias = list[
    "aws_sdk_sagemaker_geospatial.types.temporal_statistics.TemporalStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemporalStatisticsListInput) -> list:
    return list(value)


def deserialize_json(data: list) -> TemporalStatisticsListInput:
    return list(data)
