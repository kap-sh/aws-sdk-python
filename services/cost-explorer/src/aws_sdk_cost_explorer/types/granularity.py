"""Generated from Smithy shape ``com.amazonaws.costexplorer#Granularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

Granularity: TypeAlias = Literal[
    "DAILY",
    "MONTHLY",
    "HOURLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAILY",
        "MONTHLY",
        "HOURLY",
    )
)


def serialize_aws_json_1_1(value: Granularity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Granularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Granularity value: {data!r}")
    return cast(Granularity, data)
