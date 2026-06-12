"""Generated from Smithy shape ``com.amazonaws.kinesis#MetricsName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

MetricsName: TypeAlias = Literal[
    "IncomingBytes",
    "IncomingRecords",
    "OutgoingBytes",
    "OutgoingRecords",
    "WriteProvisionedThroughputExceeded",
    "ReadProvisionedThroughputExceeded",
    "IteratorAgeMilliseconds",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IncomingBytes",
        "IncomingRecords",
        "OutgoingBytes",
        "OutgoingRecords",
        "WriteProvisionedThroughputExceeded",
        "ReadProvisionedThroughputExceeded",
        "IteratorAgeMilliseconds",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: MetricsName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricsName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricsName value: {data!r}")
    return cast(MetricsName, data)
