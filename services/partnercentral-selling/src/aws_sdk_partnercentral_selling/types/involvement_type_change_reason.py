"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#InvolvementTypeChangeReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

InvolvementTypeChangeReason: TypeAlias = Literal[
    "Expansion Opportunity",
    "Change in Deal Information",
    "Customer Requested",
    "Technical Complexity",
    "Risk Mitigation",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Expansion Opportunity",
        "Change in Deal Information",
        "Customer Requested",
        "Technical Complexity",
        "Risk Mitigation",
    )
)


def serialize_aws_json_1_0(value: InvolvementTypeChangeReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvolvementTypeChangeReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InvolvementTypeChangeReason value: {data!r}"
        )
    return cast(InvolvementTypeChangeReason, data)
