"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#MatchOption``."""

from typing import Literal, TypeAlias, cast

MatchOption: TypeAlias = Literal[
    "EQUALS",
    "STARTS_WITH",
    "CONTAINS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MatchOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MatchOption:
    return cast(MatchOption, data)
