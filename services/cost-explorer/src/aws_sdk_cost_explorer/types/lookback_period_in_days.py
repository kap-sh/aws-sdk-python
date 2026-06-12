"""Generated from Smithy shape ``com.amazonaws.costexplorer#LookbackPeriodInDays``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

LookbackPeriodInDays: TypeAlias = Literal[
    "SEVEN_DAYS",
    "THIRTY_DAYS",
    "SIXTY_DAYS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEVEN_DAYS",
        "THIRTY_DAYS",
        "SIXTY_DAYS",
    )
)


def serialize_aws_json_1_1(value: LookbackPeriodInDays) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LookbackPeriodInDays:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LookbackPeriodInDays value: {data!r}")
    return cast(LookbackPeriodInDays, data)
