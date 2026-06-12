"""Generated from Smithy shape ``com.amazonaws.opensearch#PrincipalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

PrincipalType: TypeAlias = Literal[
    "AWS_ACCOUNT",
    "AWS_SERVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_ACCOUNT",
        "AWS_SERVICE",
    )
)


def serialize_json(value: PrincipalType) -> str:
    return value


def deserialize_json(data: str) -> PrincipalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrincipalType value: {data!r}")
    return cast(PrincipalType, data)
