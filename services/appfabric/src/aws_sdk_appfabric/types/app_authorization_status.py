"""Generated from Smithy shape ``com.amazonaws.appfabric#AppAuthorizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

AppAuthorizationStatus: TypeAlias = Literal[
    "PendingConnect",
    "Connected",
    "ConnectionValidationFailed",
    "TokenAutoRotationFailed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PendingConnect",
        "Connected",
        "ConnectionValidationFailed",
        "TokenAutoRotationFailed",
    )
)


def serialize_json(value: AppAuthorizationStatus) -> str:
    return value


def deserialize_json(data: str) -> AppAuthorizationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppAuthorizationStatus value: {data!r}")
    return cast(AppAuthorizationStatus, data)
