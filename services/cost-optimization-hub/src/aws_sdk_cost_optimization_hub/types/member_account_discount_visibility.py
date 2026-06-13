"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#MemberAccountDiscountVisibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

MemberAccountDiscountVisibility: TypeAlias = Literal[
    "All",
    "None",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "None",
    )
)


def serialize_aws_json_1_0(value: MemberAccountDiscountVisibility) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MemberAccountDiscountVisibility:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MemberAccountDiscountVisibility value: {data!r}"
        )
    return cast(MemberAccountDiscountVisibility, data)
