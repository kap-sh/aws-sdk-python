"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateStatistic``."""

from typing import Literal, TypeAlias, cast

"""The statistic to apply to the alarm's metric data."""
CloudWatchAlarmTemplateStatistic: TypeAlias = Literal[
    "SampleCount",
    "Average",
    "Sum",
    "Minimum",
    "Maximum",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchAlarmTemplateStatistic) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchAlarmTemplateStatistic:
    return cast(CloudWatchAlarmTemplateStatistic, data)
