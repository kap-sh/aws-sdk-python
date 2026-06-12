"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#Granularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_dashboards.errors import DeserializationError

Granularity: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "MONTHLY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOURLY",
        "DAILY",
        "MONTHLY",
    )
)


def serialize_aws_json_1_0(value: Granularity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Granularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Granularity value: {data!r}")
    return cast(Granularity, data)
