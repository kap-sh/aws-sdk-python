"""Generated from Smithy shape ``com.amazonaws.novaact#InternalServerExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_nova_act.errors import DeserializationError

InternalServerExceptionReason: TypeAlias = Literal[
    "InvalidModelGeneration",
    "RequestTokenLimitExceeded",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvalidModelGeneration",
        "RequestTokenLimitExceeded",
    )
)


def serialize_json(value: InternalServerExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> InternalServerExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InternalServerExceptionReason value: {data!r}"
        )
    return cast(InternalServerExceptionReason, data)
