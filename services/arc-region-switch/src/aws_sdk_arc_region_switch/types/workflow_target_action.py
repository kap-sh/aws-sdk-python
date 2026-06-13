"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#WorkflowTargetAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

WorkflowTargetAction: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: WorkflowTargetAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowTargetAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowTargetAction value: {data!r}")
    return cast(WorkflowTargetAction, data)
