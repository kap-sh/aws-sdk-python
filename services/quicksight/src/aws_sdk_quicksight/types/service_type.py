"""Generated from Smithy shape ``com.amazonaws.quicksight#ServiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ServiceType: TypeAlias = Literal[
    "REDSHIFT",
    "QBUSINESS",
    "ATHENA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REDSHIFT",
        "QBUSINESS",
        "ATHENA",
    )
)


def serialize_json(value: ServiceType) -> str:
    return value


def deserialize_json(data: str) -> ServiceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceType value: {data!r}")
    return cast(ServiceType, data)
