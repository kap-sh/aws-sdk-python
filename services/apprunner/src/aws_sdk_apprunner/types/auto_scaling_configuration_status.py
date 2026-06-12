"""Generated from Smithy shape ``com.amazonaws.apprunner#AutoScalingConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

AutoScalingConfigurationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_0(value: AutoScalingConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoScalingConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutoScalingConfigurationStatus value: {data!r}"
        )
    return cast(AutoScalingConfigurationStatus, data)
