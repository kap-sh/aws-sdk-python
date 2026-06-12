"""Generated from Smithy shape ``com.amazonaws.rbin#ResourceNotFoundExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

ResourceNotFoundExceptionReason: TypeAlias = Literal["RULE_NOT_FOUND",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RULE_NOT_FOUND",))


def serialize_json(value: ResourceNotFoundExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ResourceNotFoundExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceNotFoundExceptionReason value: {data!r}"
        )
    return cast(ResourceNotFoundExceptionReason, data)
