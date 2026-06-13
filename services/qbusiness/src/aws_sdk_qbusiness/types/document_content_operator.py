"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentContentOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

DocumentContentOperator: TypeAlias = Literal["DELETE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DELETE",))


def serialize_json(value: DocumentContentOperator) -> str:
    return value


def deserialize_json(data: str) -> DocumentContentOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentContentOperator value: {data!r}")
    return cast(DocumentContentOperator, data)
