"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateComparisonOperator``."""

from typing import Literal, TypeAlias, cast

"""The comparison operator used to compare the specified statistic and the threshold."""
CloudWatchAlarmTemplateComparisonOperator: TypeAlias = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanThreshold",
    "LessThanOrEqualToThreshold",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchAlarmTemplateComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchAlarmTemplateComparisonOperator:
    return cast(CloudWatchAlarmTemplateComparisonOperator, data)
