"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateServiceCode``."""

from typing import Literal, TypeAlias, cast

SavingsPlanRateServiceCode: TypeAlias = Literal[
    "AmazonEC2",
    "AmazonECS",
    "AmazonEKS",
    "AWSLambda",
    "AmazonSageMaker",
    "AmazonRDS",
    "AuroraDSQL",
    "AmazonDynamoDB",
    "AmazonElastiCache",
    "AmazonDocDB",
    "AmazonNeptune",
    "AmazonTimestream",
    "AmazonMCS",
    "AWSDatabaseMigrationSvc",
    "AmazonES",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateServiceCode) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRateServiceCode:
    return cast(SavingsPlanRateServiceCode, data)
