"""Generated from Smithy shape ``com.amazonaws.costexplorer#SupportedSavingsPlansType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

SupportedSavingsPlansType: TypeAlias = Literal[
    "COMPUTE_SP",
    "EC2_INSTANCE_SP",
    "SAGEMAKER_SP",
    "DATABASE_SP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPUTE_SP",
        "EC2_INSTANCE_SP",
        "SAGEMAKER_SP",
        "DATABASE_SP",
    )
)


def serialize_aws_json_1_1(value: SupportedSavingsPlansType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SupportedSavingsPlansType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupportedSavingsPlansType value: {data!r}")
    return cast(SupportedSavingsPlansType, data)
