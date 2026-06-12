"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricDataStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

CloudWatchMetricDataStatusCode: TypeAlias = Literal[
    "Complete",
    "InternalError",
    "PartialData",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Complete",
        "InternalError",
        "PartialData",
    )
)


def serialize_json(value: CloudWatchMetricDataStatusCode) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchMetricDataStatusCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CloudWatchMetricDataStatusCode value: {data!r}"
        )
    return cast(CloudWatchMetricDataStatusCode, data)
