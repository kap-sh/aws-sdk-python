"""Generated from Smithy shape ``com.amazonaws.appsync#BadRequestReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

"""<p>Provides context for the cause of the bad request. The only supported value is <code>CODE_ERROR</code>.</p>"""
BadRequestReason: TypeAlias = Literal["CODE_ERROR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CODE_ERROR",))


def serialize_json(value: BadRequestReason) -> str:
    return value


def deserialize_json(data: str) -> BadRequestReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BadRequestReason value: {data!r}")
    return cast(BadRequestReason, data)
