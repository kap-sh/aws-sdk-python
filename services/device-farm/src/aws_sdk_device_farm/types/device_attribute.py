"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

DeviceAttribute: TypeAlias = Literal[
    "ARN",
    "PLATFORM",
    "FORM_FACTOR",
    "MANUFACTURER",
    "REMOTE_ACCESS_ENABLED",
    "REMOTE_DEBUG_ENABLED",
    "APPIUM_VERSION",
    "INSTANCE_ARN",
    "INSTANCE_LABELS",
    "FLEET_TYPE",
    "OS_VERSION",
    "MODEL",
    "AVAILABILITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARN",
        "PLATFORM",
        "FORM_FACTOR",
        "MANUFACTURER",
        "REMOTE_ACCESS_ENABLED",
        "REMOTE_DEBUG_ENABLED",
        "APPIUM_VERSION",
        "INSTANCE_ARN",
        "INSTANCE_LABELS",
        "FLEET_TYPE",
        "OS_VERSION",
        "MODEL",
        "AVAILABILITY",
    )
)


def serialize_aws_json_1_1(value: DeviceAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceAttribute value: {data!r}")
    return cast(DeviceAttribute, data)
