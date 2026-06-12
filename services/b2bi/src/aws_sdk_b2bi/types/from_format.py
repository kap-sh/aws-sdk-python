"""Generated from Smithy shape ``com.amazonaws.b2bi#FromFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

FromFormat: TypeAlias = Literal["X12",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("X12",))


def serialize_aws_json_1_0(value: FromFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FromFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FromFormat value: {data!r}")
    return cast(FromFormat, data)
