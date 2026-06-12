"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateTargetResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The resource type this template should dynamically generate cloudwatch metric alarms for."""
CloudWatchAlarmTemplateTargetResourceType: TypeAlias = Literal[
    "CLOUDFRONT_DISTRIBUTION",
    "MEDIALIVE_MULTIPLEX",
    "MEDIALIVE_CHANNEL",
    "MEDIALIVE_INPUT_DEVICE",
    "MEDIAPACKAGE_CHANNEL",
    "MEDIAPACKAGE_ORIGIN_ENDPOINT",
    "MEDIACONNECT_FLOW",
    "S3_BUCKET",
    "MEDIATAILOR_PLAYBACK_CONFIGURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUDFRONT_DISTRIBUTION",
        "MEDIALIVE_MULTIPLEX",
        "MEDIALIVE_CHANNEL",
        "MEDIALIVE_INPUT_DEVICE",
        "MEDIAPACKAGE_CHANNEL",
        "MEDIAPACKAGE_ORIGIN_ENDPOINT",
        "MEDIACONNECT_FLOW",
        "S3_BUCKET",
        "MEDIATAILOR_PLAYBACK_CONFIGURATION",
    )
)


def serialize_json(value: CloudWatchAlarmTemplateTargetResourceType) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchAlarmTemplateTargetResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CloudWatchAlarmTemplateTargetResourceType value: {data!r}"
        )
    return cast(CloudWatchAlarmTemplateTargetResourceType, data)
