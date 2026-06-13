"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttributeValueOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

AttributeValueOperator: TypeAlias = Literal["DELETE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DELETE",))


def serialize_json(value: AttributeValueOperator) -> str:
    return value


def deserialize_json(data: str) -> AttributeValueOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeValueOperator value: {data!r}")
    return cast(AttributeValueOperator, data)
