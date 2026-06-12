"""Generated from Smithy shape ``com.amazonaws.deadline#DependenciesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_id

DependenciesList: TypeAlias = list["aws_sdk_deadline.types.step_id.StepId"]


# --- restJson1 ser/de ---
def serialize_json(value: DependenciesList) -> list:
    return list(value)


def deserialize_json(data: list) -> DependenciesList:
    return list(data)
