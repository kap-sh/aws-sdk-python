"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

DeviceFilterAttribute: TypeAlias = Literal[
    "ARN",
    "PLATFORM",
    "OS_VERSION",
    "MODEL",
    "AVAILABILITY",
    "FORM_FACTOR",
    "MANUFACTURER",
    "REMOTE_ACCESS_ENABLED",
    "REMOTE_DEBUG_ENABLED",
    "INSTANCE_ARN",
    "INSTANCE_LABELS",
    "FLEET_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARN",
        "PLATFORM",
        "OS_VERSION",
        "MODEL",
        "AVAILABILITY",
        "FORM_FACTOR",
        "MANUFACTURER",
        "REMOTE_ACCESS_ENABLED",
        "REMOTE_DEBUG_ENABLED",
        "INSTANCE_ARN",
        "INSTANCE_LABELS",
        "FLEET_TYPE",
    )
)


def serialize_aws_json_1_1(value: DeviceFilterAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceFilterAttribute value: {data!r}")
    return cast(DeviceFilterAttribute, data)
