"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceFilterAttribute``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: DeviceFilterAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceFilterAttribute:
    return cast(DeviceFilterAttribute, data)
