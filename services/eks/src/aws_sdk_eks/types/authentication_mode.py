"""Generated from Smithy shape ``com.amazonaws.eks#AuthenticationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

AuthenticationMode: TypeAlias = Literal[
    "API",
    "API_AND_CONFIG_MAP",
    "CONFIG_MAP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "API",
        "API_AND_CONFIG_MAP",
        "CONFIG_MAP",
    )
)


def serialize_json(value: AuthenticationMode) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationMode value: {data!r}")
    return cast(AuthenticationMode, data)
