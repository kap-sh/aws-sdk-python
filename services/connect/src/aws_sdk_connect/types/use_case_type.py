"""Generated from Smithy shape ``com.amazonaws.connect#UseCaseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

UseCaseType: TypeAlias = Literal[
    "RULES_EVALUATION",
    "CONNECT_CAMPAIGNS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RULES_EVALUATION",
        "CONNECT_CAMPAIGNS",
    )
)


def serialize_json(value: UseCaseType) -> str:
    return value


def deserialize_json(data: str) -> UseCaseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UseCaseType value: {data!r}")
    return cast(UseCaseType, data)
