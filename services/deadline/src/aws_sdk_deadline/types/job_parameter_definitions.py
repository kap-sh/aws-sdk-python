"""Generated from Smithy shape ``com.amazonaws.deadline#JobParameterDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_parameter_definition

JobParameterDefinitions: TypeAlias = list[
    "aws_sdk_deadline.types.job_parameter_definition.JobParameterDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobParameterDefinitions) -> list:
    return list(value)


def deserialize_json(data: list) -> JobParameterDefinitions:
    return list(data)
