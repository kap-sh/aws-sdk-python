"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ZonalStatisticsListInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.zonal_statistics

ZonalStatisticsListInput: TypeAlias = list[
    "capo_sagemaker_geospatial.types.zonal_statistics.ZonalStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: ZonalStatisticsListInput) -> list:
    return list(value)


def deserialize_json(data: list) -> ZonalStatisticsListInput:
    return list(data)
