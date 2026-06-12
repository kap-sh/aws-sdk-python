"""Generated from Smithy shape ``com.amazonaws.costexplorer#ApproximationDimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

ApproximationDimension: TypeAlias = Literal[
    "SERVICE",
    "RESOURCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE",
        "RESOURCE",
    )
)


def serialize_aws_json_1_1(value: ApproximationDimension) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApproximationDimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApproximationDimension value: {data!r}")
    return cast(ApproximationDimension, data)
