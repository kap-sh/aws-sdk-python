"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanProductType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanProductType: TypeAlias = Literal[
    "EC2",
    "Fargate",
    "Lambda",
    "SageMaker",
    "RDS",
    "DSQL",
    "DynamoDB",
    "ElastiCache",
    "DocDB",
    "Neptune",
    "Timestream",
    "Keyspaces",
    "DMS",
    "OpenSearch",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "Fargate",
        "Lambda",
        "SageMaker",
        "RDS",
        "DSQL",
        "DynamoDB",
        "ElastiCache",
        "DocDB",
        "Neptune",
        "Timestream",
        "Keyspaces",
        "DMS",
        "OpenSearch",
    )
)


def serialize_json(value: SavingsPlanProductType) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanProductType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsPlanProductType value: {data!r}")
    return cast(SavingsPlanProductType, data)
