"""Generated from Smithy shape ``com.amazonaws.devicefarm#RecurringChargeFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

RecurringChargeFrequency: TypeAlias = Literal["MONTHLY",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MONTHLY",))


def serialize_aws_json_1_1(value: RecurringChargeFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecurringChargeFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecurringChargeFrequency value: {data!r}")
    return cast(RecurringChargeFrequency, data)
