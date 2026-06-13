"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EventSourceMappingAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

EventSourceMappingAction: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
    )
)


def serialize_aws_json_1_0(value: EventSourceMappingAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EventSourceMappingAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSourceMappingAction value: {data!r}")
    return cast(EventSourceMappingAction, data)
