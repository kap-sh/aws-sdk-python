"""Generated from Smithy shape ``com.amazonaws.iot#JobTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.target_arn

JobTargets: TypeAlias = list["capo_iot.types.target_arn.TargetArn"]


# --- restJson1 ser/de ---
def serialize_json(value: JobTargets) -> list:
    return list(value)


def deserialize_json(data: list) -> JobTargets:
    return list(data)
