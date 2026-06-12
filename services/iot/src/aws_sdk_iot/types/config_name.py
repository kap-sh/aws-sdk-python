"""Generated from Smithy shape ``com.amazonaws.iot#ConfigName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ConfigName: TypeAlias = Literal[
    "CERT_AGE_THRESHOLD_IN_DAYS",
    "CERT_EXPIRATION_THRESHOLD_IN_DAYS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CERT_AGE_THRESHOLD_IN_DAYS",
        "CERT_EXPIRATION_THRESHOLD_IN_DAYS",
    )
)


def serialize_json(value: ConfigName) -> str:
    return value


def deserialize_json(data: str) -> ConfigName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigName value: {data!r}")
    return cast(ConfigName, data)
