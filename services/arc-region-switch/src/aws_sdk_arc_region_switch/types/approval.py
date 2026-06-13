"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Approval``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

Approval: TypeAlias = Literal[
    "approve",
    "decline",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "approve",
        "decline",
    )
)


def serialize_aws_json_1_0(value: Approval) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Approval:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Approval value: {data!r}")
    return cast(Approval, data)
