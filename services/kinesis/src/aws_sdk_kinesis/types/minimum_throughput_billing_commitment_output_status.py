"""Generated from Smithy shape ``com.amazonaws.kinesis#MinimumThroughputBillingCommitmentOutputStatus``."""

from typing import Literal, TypeAlias, cast

MinimumThroughputBillingCommitmentOutputStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLED_UNTIL_EARLIEST_ALLOWED_END",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MinimumThroughputBillingCommitmentOutputStatus,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> MinimumThroughputBillingCommitmentOutputStatus:
    return cast(MinimumThroughputBillingCommitmentOutputStatus, data)
