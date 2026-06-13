"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionStepAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

UpdatePlanExecutionStepAction: TypeAlias = Literal[
    "switchToUngraceful",
    "skip",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "switchToUngraceful",
        "skip",
    )
)


def serialize_aws_json_1_0(value: UpdatePlanExecutionStepAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdatePlanExecutionStepAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UpdatePlanExecutionStepAction value: {data!r}"
        )
    return cast(UpdatePlanExecutionStepAction, data)
