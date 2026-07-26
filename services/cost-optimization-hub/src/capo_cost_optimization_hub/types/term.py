"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Term``."""

from typing import Literal, TypeAlias, cast

Term: TypeAlias = Literal[
    "OneYear",
    "ThreeYears",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Term) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Term:
    return cast(Term, data)
