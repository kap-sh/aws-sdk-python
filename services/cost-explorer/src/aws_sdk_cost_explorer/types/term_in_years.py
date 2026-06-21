"""Generated from Smithy shape ``com.amazonaws.costexplorer#TermInYears``."""

from typing import Literal, TypeAlias, cast

TermInYears: TypeAlias = Literal[
    "ONE_YEAR",
    "THREE_YEARS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermInYears) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TermInYears:
    return cast(TermInYears, data)
