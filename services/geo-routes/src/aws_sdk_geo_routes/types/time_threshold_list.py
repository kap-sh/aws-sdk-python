"""Generated from Smithy shape ``com.amazonaws.georoutes#TimeThresholdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds

TimeThresholdList: TypeAlias = list[
    "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeThresholdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TimeThresholdList:
    return list(data)
