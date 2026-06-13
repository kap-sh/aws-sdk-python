"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ApplicationDiscoveryStatus: TypeAlias = Literal[
    "SUCCESS",
    "REGISTRATION_FAILED",
    "REFRESH_FAILED",
    "REGISTERING",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "REGISTRATION_FAILED",
        "REFRESH_FAILED",
        "REGISTERING",
        "DELETING",
    )
)


def serialize_json(value: ApplicationDiscoveryStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationDiscoveryStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ApplicationDiscoveryStatus value: {data!r}"
        )
    return cast(ApplicationDiscoveryStatus, data)
