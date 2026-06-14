"""Generated from Smithy shape ``com.amazonaws.datazone#AuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

AuthType: TypeAlias = Literal[
    "IAM_IDC",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM_IDC",
        "DISABLED",
    )
)


def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthType value: {data!r}")
    return cast(AuthType, data)
