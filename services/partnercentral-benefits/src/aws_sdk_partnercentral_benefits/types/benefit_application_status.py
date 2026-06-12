"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitApplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_benefits.errors import DeserializationError

BenefitApplicationStatus: TypeAlias = Literal[
    "PENDING_SUBMISSION",
    "IN_REVIEW",
    "ACTION_REQUIRED",
    "APPROVED",
    "REJECTED",
    "CANCELED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_SUBMISSION",
        "IN_REVIEW",
        "ACTION_REQUIRED",
        "APPROVED",
        "REJECTED",
        "CANCELED",
    )
)


def serialize_aws_json_1_0(value: BenefitApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BenefitApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BenefitApplicationStatus value: {data!r}")
    return cast(BenefitApplicationStatus, data)
