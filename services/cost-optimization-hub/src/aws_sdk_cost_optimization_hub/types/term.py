"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Term``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

Term: TypeAlias = Literal[
    "OneYear",
    "ThreeYears",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OneYear",
        "ThreeYears",
    )
)


def serialize_aws_json_1_0(value: Term) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Term:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Term value: {data!r}")
    return cast(Term, data)
