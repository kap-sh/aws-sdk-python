"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandProvisioningAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

OnDemandProvisioningAllocationStrategy: TypeAlias = Literal[
    "lowest-price",
    "prioritized",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "lowest-price",
        "prioritized",
    )
)


def serialize_aws_json_1_1(value: OnDemandProvisioningAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnDemandProvisioningAllocationStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OnDemandProvisioningAllocationStrategy value: {data!r}"
        )
    return cast(OnDemandProvisioningAllocationStrategy, data)
