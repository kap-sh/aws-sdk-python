"""Generated from Smithy shape ``com.amazonaws.costexplorer#MonitorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

MonitorType: TypeAlias = Literal[
    "DIMENSIONAL",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIMENSIONAL",
        "CUSTOM",
    )
)


def serialize_aws_json_1_1(value: MonitorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorType value: {data!r}")
    return cast(MonitorType, data)
