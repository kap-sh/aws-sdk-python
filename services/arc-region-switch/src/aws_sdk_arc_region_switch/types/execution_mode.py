"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

ExecutionMode: TypeAlias = Literal[
    "graceful",
    "ungraceful",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "graceful",
        "ungraceful",
    )
)


def serialize_aws_json_1_0(value: ExecutionMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionMode value: {data!r}")
    return cast(ExecutionMode, data)
