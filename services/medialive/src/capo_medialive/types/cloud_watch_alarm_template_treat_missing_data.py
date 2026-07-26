"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateTreatMissingData``."""

from typing import Literal, TypeAlias, cast

"""Specifies how missing data points are treated when evaluating the alarm's condition."""
CloudWatchAlarmTemplateTreatMissingData: TypeAlias = Literal[
    "notBreaching",
    "breaching",
    "ignore",
    "missing",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchAlarmTemplateTreatMissingData) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchAlarmTemplateTreatMissingData:
    return cast(CloudWatchAlarmTemplateTreatMissingData, data)
