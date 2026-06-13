"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

UpdatePlanExecutionAction: TypeAlias = Literal[
    "switchToGraceful",
    "switchToUngraceful",
    "pause",
    "resume",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "switchToGraceful",
        "switchToUngraceful",
        "pause",
        "resume",
    )
)


def serialize_aws_json_1_0(value: UpdatePlanExecutionAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdatePlanExecutionAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdatePlanExecutionAction value: {data!r}")
    return cast(UpdatePlanExecutionAction, data)
