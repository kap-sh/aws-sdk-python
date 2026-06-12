"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The comparison operator used to compare the specified statistic and the threshold."""
CloudWatchAlarmTemplateComparisonOperator: TypeAlias = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanThreshold",
    "LessThanOrEqualToThreshold",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GreaterThanOrEqualToThreshold",
        "GreaterThanThreshold",
        "LessThanThreshold",
        "LessThanOrEqualToThreshold",
    )
)


def serialize_json(value: CloudWatchAlarmTemplateComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchAlarmTemplateComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CloudWatchAlarmTemplateComparisonOperator value: {data!r}"
        )
    return cast(CloudWatchAlarmTemplateComparisonOperator, data)
