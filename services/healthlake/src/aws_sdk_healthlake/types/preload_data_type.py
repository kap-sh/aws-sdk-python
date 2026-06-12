"""Generated from Smithy shape ``com.amazonaws.healthlake#PreloadDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

PreloadDataType: TypeAlias = Literal["SYNTHEA",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SYNTHEA",))


def serialize_aws_json_1_0(value: PreloadDataType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PreloadDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreloadDataType value: {data!r}")
    return cast(PreloadDataType, data)
