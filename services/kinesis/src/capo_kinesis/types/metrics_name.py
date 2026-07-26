"""Generated from Smithy shape ``com.amazonaws.kinesis#MetricsName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: MetricsName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricsName:
    return cast(MetricsName, data)
