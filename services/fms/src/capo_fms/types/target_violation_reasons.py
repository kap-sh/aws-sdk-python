"""Generated from Smithy shape ``com.amazonaws.fms#TargetViolationReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.target_violation_reason

TargetViolationReasons: TypeAlias = list[
    "capo_fms.types.target_violation_reason.TargetViolationReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetViolationReasons) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetViolationReasons:
    return list(data)
