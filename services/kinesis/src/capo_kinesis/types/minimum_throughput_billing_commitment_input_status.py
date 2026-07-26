"""Generated from Smithy shape ``com.amazonaws.kinesis#MinimumThroughputBillingCommitmentInputStatus``."""

from typing import Literal, TypeAlias, cast

MinimumThroughputBillingCommitmentInputStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MinimumThroughputBillingCommitmentInputStatus) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> MinimumThroughputBillingCommitmentInputStatus:
    return cast(MinimumThroughputBillingCommitmentInputStatus, data)
