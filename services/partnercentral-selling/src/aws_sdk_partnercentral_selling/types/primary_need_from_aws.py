"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#PrimaryNeedFromAws``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

PrimaryNeedFromAws: TypeAlias = Literal[
    "Co-Sell - Architectural Validation",
    "Co-Sell - Business Presentation",
    "Co-Sell - Competitive Information",
    "Co-Sell - Pricing Assistance",
    "Co-Sell - Technical Consultation",
    "Co-Sell - Total Cost of Ownership Evaluation",
    "Co-Sell - Deal Support",
    "Co-Sell - Support for Public Tender / RFx",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Co-Sell - Architectural Validation",
        "Co-Sell - Business Presentation",
        "Co-Sell - Competitive Information",
        "Co-Sell - Pricing Assistance",
        "Co-Sell - Technical Consultation",
        "Co-Sell - Total Cost of Ownership Evaluation",
        "Co-Sell - Deal Support",
        "Co-Sell - Support for Public Tender / RFx",
    )
)


def serialize_aws_json_1_0(value: PrimaryNeedFromAws) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PrimaryNeedFromAws:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrimaryNeedFromAws value: {data!r}")
    return cast(PrimaryNeedFromAws, data)
