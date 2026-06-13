"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ResourceWarningStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

ResourceWarningStatus: TypeAlias = Literal[
    "active",
    "resolved",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "resolved",
    )
)


def serialize_aws_json_1_0(value: ResourceWarningStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceWarningStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceWarningStatus value: {data!r}")
    return cast(ResourceWarningStatus, data)
