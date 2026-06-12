"""Generated from Smithy shape ``com.amazonaws.deadline#StepParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_parameter

StepParameterList: TypeAlias = list[
    "aws_sdk_deadline.types.step_parameter.StepParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: StepParameterList) -> list:
    import aws_sdk_deadline.types.step_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.step_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepParameterList:
    import aws_sdk_deadline.types.step_parameter

    out: StepParameterList = []
    for item in data:
        out.append(aws_sdk_deadline.types.step_parameter.deserialize_json(item))
    return out
