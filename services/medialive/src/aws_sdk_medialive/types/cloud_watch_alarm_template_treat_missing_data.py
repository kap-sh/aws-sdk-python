"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateTreatMissingData``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Specifies how missing data points are treated when evaluating the alarm's condition."""
CloudWatchAlarmTemplateTreatMissingData: TypeAlias = Literal[
    "notBreaching",
    "breaching",
    "ignore",
    "missing",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "notBreaching",
        "breaching",
        "ignore",
        "missing",
    )
)


def serialize_json(value: CloudWatchAlarmTemplateTreatMissingData) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchAlarmTemplateTreatMissingData:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CloudWatchAlarmTemplateTreatMissingData value: {data!r}"
        )
    return cast(CloudWatchAlarmTemplateTreatMissingData, data)
