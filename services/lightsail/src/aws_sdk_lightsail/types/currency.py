"""Generated from Smithy shape ``com.amazonaws.lightsail#Currency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

Currency: TypeAlias = Literal["USD",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_aws_json_1_1(value: Currency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Currency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Currency value: {data!r}")
    return cast(Currency, data)
