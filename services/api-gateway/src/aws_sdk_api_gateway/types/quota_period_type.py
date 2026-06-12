"""Generated from Smithy shape ``com.amazonaws.apigateway#QuotaPeriodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

QuotaPeriodType: TypeAlias = Literal[
    "DAY",
    "WEEK",
    "MONTH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAY",
        "WEEK",
        "MONTH",
    )
)


def serialize_json(value: QuotaPeriodType) -> str:
    return value


def deserialize_json(data: str) -> QuotaPeriodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuotaPeriodType value: {data!r}")
    return cast(QuotaPeriodType, data)
