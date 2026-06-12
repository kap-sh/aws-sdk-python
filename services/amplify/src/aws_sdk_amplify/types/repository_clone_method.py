"""Generated from Smithy shape ``com.amazonaws.amplify#RepositoryCloneMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

RepositoryCloneMethod: TypeAlias = Literal[
    "SSH",
    "TOKEN",
    "SIGV4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSH",
        "TOKEN",
        "SIGV4",
    )
)


def serialize_json(value: RepositoryCloneMethod) -> str:
    return value


def deserialize_json(data: str) -> RepositoryCloneMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RepositoryCloneMethod value: {data!r}")
    return cast(RepositoryCloneMethod, data)
