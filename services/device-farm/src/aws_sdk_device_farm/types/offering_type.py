"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

OfferingType: TypeAlias = Literal["RECURRING",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RECURRING",))


def serialize_aws_json_1_1(value: OfferingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OfferingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferingType value: {data!r}")
    return cast(OfferingType, data)
