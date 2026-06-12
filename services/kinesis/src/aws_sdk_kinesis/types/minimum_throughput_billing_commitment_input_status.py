"""Generated from Smithy shape ``com.amazonaws.kinesis#MinimumThroughputBillingCommitmentInputStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

MinimumThroughputBillingCommitmentInputStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: MinimumThroughputBillingCommitmentInputStatus) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> MinimumThroughputBillingCommitmentInputStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MinimumThroughputBillingCommitmentInputStatus value: {data!r}"
        )
    return cast(MinimumThroughputBillingCommitmentInputStatus, data)
