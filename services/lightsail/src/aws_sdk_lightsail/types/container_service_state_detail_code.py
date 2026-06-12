"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceStateDetailCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContainerServiceStateDetailCode: TypeAlias = Literal[
    "CREATING_SYSTEM_RESOURCES",
    "CREATING_NETWORK_INFRASTRUCTURE",
    "PROVISIONING_CERTIFICATE",
    "PROVISIONING_SERVICE",
    "CREATING_DEPLOYMENT",
    "EVALUATING_HEALTH_CHECK",
    "ACTIVATING_DEPLOYMENT",
    "CERTIFICATE_LIMIT_EXCEEDED",
    "UNKNOWN_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING_SYSTEM_RESOURCES",
        "CREATING_NETWORK_INFRASTRUCTURE",
        "PROVISIONING_CERTIFICATE",
        "PROVISIONING_SERVICE",
        "CREATING_DEPLOYMENT",
        "EVALUATING_HEALTH_CHECK",
        "ACTIVATING_DEPLOYMENT",
        "CERTIFICATE_LIMIT_EXCEEDED",
        "UNKNOWN_ERROR",
    )
)


def serialize_aws_json_1_1(value: ContainerServiceStateDetailCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceStateDetailCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerServiceStateDetailCode value: {data!r}"
        )
    return cast(ContainerServiceStateDetailCode, data)
