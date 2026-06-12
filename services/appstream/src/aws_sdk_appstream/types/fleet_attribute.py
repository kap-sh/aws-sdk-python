"""Generated from Smithy shape ``com.amazonaws.appstream#FleetAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""<p>The fleet attribute.</p>"""
FleetAttribute: TypeAlias = Literal[
    "VPC_CONFIGURATION",
    "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
    "DOMAIN_JOIN_INFO",
    "IAM_ROLE_ARN",
    "USB_DEVICE_FILTER_STRINGS",
    "SESSION_SCRIPT_S3_LOCATION",
    "MAX_SESSIONS_PER_INSTANCE",
    "VOLUME_CONFIGURATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VPC_CONFIGURATION",
        "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
        "DOMAIN_JOIN_INFO",
        "IAM_ROLE_ARN",
        "USB_DEVICE_FILTER_STRINGS",
        "SESSION_SCRIPT_S3_LOCATION",
        "MAX_SESSIONS_PER_INSTANCE",
        "VOLUME_CONFIGURATION",
    )
)


def serialize_aws_json_1_1(value: FleetAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetAttribute value: {data!r}")
    return cast(FleetAttribute, data)
