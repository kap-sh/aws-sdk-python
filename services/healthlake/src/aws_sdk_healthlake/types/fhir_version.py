"""Generated from Smithy shape ``com.amazonaws.healthlake#FHIRVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

FHIRVersion: TypeAlias = Literal["R4",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("R4",))


def serialize_aws_json_1_0(value: FHIRVersion) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FHIRVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FHIRVersion value: {data!r}")
    return cast(FHIRVersion, data)
