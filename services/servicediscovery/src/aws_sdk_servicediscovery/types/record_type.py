"""Generated from Smithy shape ``com.amazonaws.servicediscovery#RecordType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

RecordType: TypeAlias = Literal[
    "SRV",
    "A",
    "AAAA",
    "CNAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SRV",
        "A",
        "AAAA",
        "CNAME",
    )
)


def serialize_aws_json_1_1(value: RecordType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordType value: {data!r}")
    return cast(RecordType, data)
