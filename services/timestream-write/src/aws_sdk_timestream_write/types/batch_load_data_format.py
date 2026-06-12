"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

BatchLoadDataFormat: TypeAlias = Literal["CSV",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CSV",))


def serialize_aws_json_1_0(value: BatchLoadDataFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchLoadDataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchLoadDataFormat value: {data!r}")
    return cast(BatchLoadDataFormat, data)
