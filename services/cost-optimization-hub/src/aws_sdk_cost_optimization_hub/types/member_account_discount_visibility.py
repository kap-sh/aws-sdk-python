"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#MemberAccountDiscountVisibility``."""

from typing import Literal, TypeAlias, cast

MemberAccountDiscountVisibility: TypeAlias = Literal[
    "All",
    "None",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemberAccountDiscountVisibility) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MemberAccountDiscountVisibility:
    return cast(MemberAccountDiscountVisibility, data)
