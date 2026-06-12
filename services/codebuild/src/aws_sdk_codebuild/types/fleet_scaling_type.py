"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetScalingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetScalingType: TypeAlias = Literal["TARGET_TRACKING_SCALING",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TARGET_TRACKING_SCALING",))


def serialize_aws_json_1_1(value: FleetScalingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetScalingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetScalingType value: {data!r}")
    return cast(FleetScalingType, data)
