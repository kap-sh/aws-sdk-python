"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UnAuthenticatedElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

UnAuthenticatedElement: TypeAlias = Literal[
    "READ",
    "CREATE_AND_UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "CREATE_AND_UPDATE",
        "DELETE",
    )
)


def serialize_json(value: UnAuthenticatedElement) -> str:
    return value


def deserialize_json(data: str) -> UnAuthenticatedElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UnAuthenticatedElement value: {data!r}")
    return cast(UnAuthenticatedElement, data)
