"""Generated from Smithy shape ``com.amazonaws.appflow#PrivateConnectionProvisioningFailureCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

PrivateConnectionProvisioningFailureCause: TypeAlias = Literal[
    "CONNECTOR_AUTHENTICATION",
    "CONNECTOR_SERVER",
    "INTERNAL_SERVER",
    "ACCESS_DENIED",
    "VALIDATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTOR_AUTHENTICATION",
        "CONNECTOR_SERVER",
        "INTERNAL_SERVER",
        "ACCESS_DENIED",
        "VALIDATION",
    )
)


def serialize_json(value: PrivateConnectionProvisioningFailureCause) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionProvisioningFailureCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PrivateConnectionProvisioningFailureCause value: {data!r}"
        )
    return cast(PrivateConnectionProvisioningFailureCause, data)
