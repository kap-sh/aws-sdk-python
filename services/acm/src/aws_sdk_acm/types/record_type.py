"""Generated from Smithy shape ``com.amazonaws.acm#RecordType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

RecordType: TypeAlias = Literal["CNAME",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CNAME",))


def serialize_aws_json_1_1(value: RecordType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordType value: {data!r}")
    return cast(RecordType, data)
