"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

CapabilityType: TypeAlias = Literal["edi",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("edi",))


def serialize_aws_json_1_0(value: CapabilityType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CapabilityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityType value: {data!r}")
    return cast(CapabilityType, data)
