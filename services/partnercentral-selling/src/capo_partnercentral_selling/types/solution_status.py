"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SolutionStatus``."""

from typing import Literal, TypeAlias, cast

SolutionStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
    "Draft",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SolutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SolutionStatus:
    return cast(SolutionStatus, data)
