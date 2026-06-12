"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The statistic to apply to the alarm's metric data."""
CloudWatchAlarmTemplateStatistic: TypeAlias = Literal[
    "SampleCount",
    "Average",
    "Sum",
    "Minimum",
    "Maximum",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SampleCount",
        "Average",
        "Sum",
        "Minimum",
        "Maximum",
    )
)


def serialize_json(value: CloudWatchAlarmTemplateStatistic) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchAlarmTemplateStatistic:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CloudWatchAlarmTemplateStatistic value: {data!r}"
        )
    return cast(CloudWatchAlarmTemplateStatistic, data)
