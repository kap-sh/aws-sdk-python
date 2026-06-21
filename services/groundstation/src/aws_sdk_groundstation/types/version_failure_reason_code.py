"""Generated from Smithy shape ``com.amazonaws.groundstation#VersionFailureReasonCode``."""

from typing import Literal, TypeAlias, cast

VersionFailureReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "INVALID_SATELLITE_ARN",
    "INVALID_UPDATE_CONTACT_REQUEST",
    "EPHEMERIS_NOT_FOUND",
    "EPHEMERIS_TIME_RANGE_INVALID",
    "EPHEMERIS_NOT_ENABLED",
    "SATELLITE_DOES_NOT_MATCH_EPHEMERIS",
    "NOT_ONBOARDED_TO_AZEL_EPHEMERIS",
    "AZEL_EPHEMERIS_NOT_FOUND",
    "AZEL_EPHEMERIS_WRONG_GROUND_STATION",
    "AZEL_EPHEMERIS_INVALID_STATUS",
    "AZEL_EPHEMERIS_TIME_RANGE_INVALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionFailureReasonCode) -> str:
    return value


def deserialize_json(data: str) -> VersionFailureReasonCode:
    return cast(VersionFailureReasonCode, data)
