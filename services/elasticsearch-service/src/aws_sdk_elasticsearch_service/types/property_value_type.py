"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PropertyValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

PropertyValueType: TypeAlias = Literal[
    "PLAIN_TEXT",
    "STRINGIFIED_JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLAIN_TEXT",
        "STRINGIFIED_JSON",
    )
)


def serialize_json(value: PropertyValueType) -> str:
    return value


def deserialize_json(data: str) -> PropertyValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropertyValueType value: {data!r}")
    return cast(PropertyValueType, data)
