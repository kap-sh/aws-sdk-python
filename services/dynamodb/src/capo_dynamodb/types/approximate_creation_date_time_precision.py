"""Generated from Smithy shape ``com.amazonaws.dynamodb#ApproximateCreationDateTimePrecision``."""

from typing import Literal, TypeAlias, cast

ApproximateCreationDateTimePrecision: TypeAlias = Literal[
    "MILLISECOND",
    "MICROSECOND",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ApproximateCreationDateTimePrecision) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ApproximateCreationDateTimePrecision:
    return cast(ApproximateCreationDateTimePrecision, data)
