"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitAllocationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_benefits.errors import DeserializationError

BenefitAllocationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "FULFILLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "FULFILLED",
    )
)


def serialize_aws_json_1_0(value: BenefitAllocationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BenefitAllocationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BenefitAllocationStatus value: {data!r}")
    return cast(BenefitAllocationStatus, data)
