"""Generated from Smithy shape ``com.amazonaws.b2bi#ToFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

ToFormat: TypeAlias = Literal["X12",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("X12",))


def serialize_aws_json_1_0(value: ToFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ToFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ToFormat value: {data!r}")
    return cast(ToFormat, data)
