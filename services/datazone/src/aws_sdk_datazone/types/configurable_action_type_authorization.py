"""Generated from Smithy shape ``com.amazonaws.datazone#ConfigurableActionTypeAuthorization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ConfigurableActionTypeAuthorization: TypeAlias = Literal[
    "IAM",
    "HTTPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "HTTPS",
    )
)


def serialize_json(value: ConfigurableActionTypeAuthorization) -> str:
    return value


def deserialize_json(data: str) -> ConfigurableActionTypeAuthorization:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigurableActionTypeAuthorization value: {data!r}"
        )
    return cast(ConfigurableActionTypeAuthorization, data)
