"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchFieldOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

SearchFieldOperator: TypeAlias = Literal[
    "EQUALS",
    "INCLUDES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "INCLUDES",
    )
)


def serialize_json(value: SearchFieldOperator) -> str:
    return value


def deserialize_json(data: str) -> SearchFieldOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchFieldOperator value: {data!r}")
    return cast(SearchFieldOperator, data)
