"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

ExecutionAction: TypeAlias = Literal[
    "activate",
    "deactivate",
    "postRecovery",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "activate",
        "deactivate",
        "postRecovery",
    )
)


def serialize_aws_json_1_0(value: ExecutionAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionAction value: {data!r}")
    return cast(ExecutionAction, data)
