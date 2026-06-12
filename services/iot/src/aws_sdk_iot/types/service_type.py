"""Generated from Smithy shape ``com.amazonaws.iot#ServiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ServiceType: TypeAlias = Literal[
    "DATA",
    "CREDENTIAL_PROVIDER",
    "JOBS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATA",
        "CREDENTIAL_PROVIDER",
        "JOBS",
    )
)


def serialize_json(value: ServiceType) -> str:
    return value


def deserialize_json(data: str) -> ServiceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceType value: {data!r}")
    return cast(ServiceType, data)
