"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SalesActivity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

SalesActivity: TypeAlias = Literal[
    "Initialized discussions with customer",
    "Customer has shown interest in solution",
    "Conducted POC / Demo",
    "In evaluation / planning stage",
    "Agreed on solution to Business Problem",
    "Completed Action Plan",
    "Finalized Deployment Need",
    "SOW Signed",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Initialized discussions with customer",
        "Customer has shown interest in solution",
        "Conducted POC / Demo",
        "In evaluation / planning stage",
        "Agreed on solution to Business Problem",
        "Completed Action Plan",
        "Finalized Deployment Need",
        "SOW Signed",
    )
)


def serialize_aws_json_1_0(value: SalesActivity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SalesActivity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SalesActivity value: {data!r}")
    return cast(SalesActivity, data)
