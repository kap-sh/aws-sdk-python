"""Generated from Smithy shape ``com.amazonaws.freetier#CurrencyCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_freetier.errors import DeserializationError

CurrencyCode: TypeAlias = Literal["USD",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_aws_json_1_0(value: CurrencyCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CurrencyCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CurrencyCode value: {data!r}")
    return cast(CurrencyCode, data)
