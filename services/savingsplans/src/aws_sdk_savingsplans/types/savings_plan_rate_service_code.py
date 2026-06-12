"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateServiceCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: SavingsPlanRateServiceCode) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRateServiceCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SavingsPlanRateServiceCode value: {data!r}"
        )
    return cast(SavingsPlanRateServiceCode, data)
