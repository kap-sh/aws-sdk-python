"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#MatchOption``."""

from typing import Literal, TypeAlias, cast

MatchOption: TypeAlias = Literal[
    "EQUALS",
    "ABSENT",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "GREATER_THAN_OR_EQUAL",
    "CASE_SENSITIVE",
    "CASE_INSENSITIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MatchOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MatchOption:
    return cast(MatchOption, data)
