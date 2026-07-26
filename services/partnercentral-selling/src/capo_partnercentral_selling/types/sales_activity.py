"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SalesActivity``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: SalesActivity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SalesActivity:
    return cast(SalesActivity, data)
