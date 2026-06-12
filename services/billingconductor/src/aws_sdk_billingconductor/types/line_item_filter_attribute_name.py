"""Generated from Smithy shape ``com.amazonaws.billingconductor#LineItemFilterAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

LineItemFilterAttributeName: TypeAlias = Literal[
    "LINE_ITEM_TYPE",
    "SERVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINE_ITEM_TYPE",
        "SERVICE",
    )
)


def serialize_json(value: LineItemFilterAttributeName) -> str:
    return value


def deserialize_json(data: str) -> LineItemFilterAttributeName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LineItemFilterAttributeName value: {data!r}"
        )
    return cast(LineItemFilterAttributeName, data)
