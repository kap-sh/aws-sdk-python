"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricDataStatusCode``."""

from typing import Literal, TypeAlias, cast

CloudWatchMetricDataStatusCode: TypeAlias = Literal[
    "Complete",
    "InternalError",
    "PartialData",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMetricDataStatusCode) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchMetricDataStatusCode:
    return cast(CloudWatchMetricDataStatusCode, data)
