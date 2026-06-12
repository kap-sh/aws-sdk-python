"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ClosedLostReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

ClosedLostReason: TypeAlias = Literal[
    "Customer Deficiency",
    "Delay / Cancellation of Project",
    "Legal / Tax / Regulatory",
    "Lost to Competitor - Google",
    "Lost to Competitor - Microsoft",
    "Lost to Competitor - SoftLayer",
    "Lost to Competitor - VMWare",
    "Lost to Competitor - Other",
    "No Opportunity",
    "On Premises Deployment",
    "Partner Gap",
    "Price",
    "Security / Compliance",
    "Technical Limitations",
    "Customer Experience",
    "Other",
    "People/Relationship/Governance",
    "Product/Technology",
    "Financial/Commercial",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Customer Deficiency",
        "Delay / Cancellation of Project",
        "Legal / Tax / Regulatory",
        "Lost to Competitor - Google",
        "Lost to Competitor - Microsoft",
        "Lost to Competitor - SoftLayer",
        "Lost to Competitor - VMWare",
        "Lost to Competitor - Other",
        "No Opportunity",
        "On Premises Deployment",
        "Partner Gap",
        "Price",
        "Security / Compliance",
        "Technical Limitations",
        "Customer Experience",
        "Other",
        "People/Relationship/Governance",
        "Product/Technology",
        "Financial/Commercial",
    )
)


def serialize_aws_json_1_0(value: ClosedLostReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ClosedLostReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClosedLostReason value: {data!r}")
    return cast(ClosedLostReason, data)
