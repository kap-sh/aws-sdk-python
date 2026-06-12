"""Generated from Smithy shape ``com.amazonaws.kinesis#MinimumThroughputBillingCommitmentOutputStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

MinimumThroughputBillingCommitmentOutputStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLED_UNTIL_EARLIEST_ALLOWED_END",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "ENABLED_UNTIL_EARLIEST_ALLOWED_END",
    )
)


def serialize_aws_json_1_1(
    value: MinimumThroughputBillingCommitmentOutputStatus,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> MinimumThroughputBillingCommitmentOutputStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MinimumThroughputBillingCommitmentOutputStatus value: {data!r}"
        )
    return cast(MinimumThroughputBillingCommitmentOutputStatus, data)
