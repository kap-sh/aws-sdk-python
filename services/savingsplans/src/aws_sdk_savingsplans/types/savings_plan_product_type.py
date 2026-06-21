"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanProductType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SavingsPlanProductType) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanProductType:
    return cast(SavingsPlanProductType, data)
