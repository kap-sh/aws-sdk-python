"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_benefits.errors import DeserializationError

BenefitStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_0(value: BenefitStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BenefitStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BenefitStatus value: {data!r}")
    return cast(BenefitStatus, data)
