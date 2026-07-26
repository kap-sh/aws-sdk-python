"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SolutionSortName``."""

from typing import Literal, TypeAlias, cast

SolutionSortName: TypeAlias = Literal[
    "Identifier",
    "Name",
    "Status",
    "Category",
    "CreatedDate",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SolutionSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SolutionSortName:
    return cast(SolutionSortName, data)
