"""Generated from Smithy shape ``com.amazonaws.iot#TargetViolationIdsForDetectMitigationActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.violation_id

TargetViolationIdsForDetectMitigationActions: TypeAlias = list[
    "aws_sdk_iot.types.violation_id.ViolationId"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetViolationIdsForDetectMitigationActions) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetViolationIdsForDetectMitigationActions:
    return list(data)
