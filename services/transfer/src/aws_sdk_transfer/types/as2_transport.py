"""Generated from Smithy shape ``com.amazonaws.transfer#As2Transport``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

As2Transport: TypeAlias = Literal["HTTP",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HTTP",))


def serialize_aws_json_1_1(value: As2Transport) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> As2Transport:
    if data not in _VALUES:
        raise DeserializationError(f"unknown As2Transport value: {data!r}")
    return cast(As2Transport, data)
