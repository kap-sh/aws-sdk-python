"""Generated from Smithy shape ``com.amazonaws.forecast#Domain``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

Domain: TypeAlias = Literal[
    "RETAIL",
    "CUSTOM",
    "INVENTORY_PLANNING",
    "EC2_CAPACITY",
    "WORK_FORCE",
    "WEB_TRAFFIC",
    "METRICS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RETAIL",
        "CUSTOM",
        "INVENTORY_PLANNING",
        "EC2_CAPACITY",
        "WORK_FORCE",
        "WEB_TRAFFIC",
        "METRICS",
    )
)


def serialize_aws_json_1_1(value: Domain) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Domain:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Domain value: {data!r}")
    return cast(Domain, data)
