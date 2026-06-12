"""Generated from Smithy shape ``com.amazonaws.costexplorer#MonitorDimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

MonitorDimension: TypeAlias = Literal[
    "SERVICE",
    "LINKED_ACCOUNT",
    "TAG",
    "COST_CATEGORY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE",
        "LINKED_ACCOUNT",
        "TAG",
        "COST_CATEGORY",
    )
)


def serialize_aws_json_1_1(value: MonitorDimension) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitorDimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorDimension value: {data!r}")
    return cast(MonitorDimension, data)
