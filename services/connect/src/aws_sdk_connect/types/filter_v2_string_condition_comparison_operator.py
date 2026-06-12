"""Generated from Smithy shape ``com.amazonaws.connect#FilterV2StringConditionComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

FilterV2StringConditionComparisonOperator: TypeAlias = Literal["NOT_EXISTS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NOT_EXISTS",))


def serialize_json(value: FilterV2StringConditionComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterV2StringConditionComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FilterV2StringConditionComparisonOperator value: {data!r}"
        )
    return cast(FilterV2StringConditionComparisonOperator, data)
