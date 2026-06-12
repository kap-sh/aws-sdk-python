"""Generated from Smithy shape ``com.amazonaws.iot#DomainConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DomainConfigurationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DomainConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainConfigurationStatus value: {data!r}")
    return cast(DomainConfigurationStatus, data)
