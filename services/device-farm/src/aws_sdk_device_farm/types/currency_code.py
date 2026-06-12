"""Generated from Smithy shape ``com.amazonaws.devicefarm#CurrencyCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

CurrencyCode: TypeAlias = Literal["USD",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_aws_json_1_1(value: CurrencyCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CurrencyCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CurrencyCode value: {data!r}")
    return cast(CurrencyCode, data)
