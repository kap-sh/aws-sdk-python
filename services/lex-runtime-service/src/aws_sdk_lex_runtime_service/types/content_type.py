"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#ContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_service.errors import DeserializationError

ContentType: TypeAlias = Literal["application/vnd.amazonaws.card.generic",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("application/vnd.amazonaws.card.generic",))


def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)
