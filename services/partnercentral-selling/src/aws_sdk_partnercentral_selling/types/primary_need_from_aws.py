"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#PrimaryNeedFromAws``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: PrimaryNeedFromAws) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PrimaryNeedFromAws:
    return cast(PrimaryNeedFromAws, data)
