"""Generated from Smithy shape ``com.amazonaws.appflow#PrivateConnectionProvisioningStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

PrivateConnectionProvisioningStatus: TypeAlias = Literal[
    "FAILED",
    "PENDING",
    "CREATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "PENDING",
        "CREATED",
    )
)


def serialize_json(value: PrivateConnectionProvisioningStatus) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionProvisioningStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PrivateConnectionProvisioningStatus value: {data!r}"
        )
    return cast(PrivateConnectionProvisioningStatus, data)
