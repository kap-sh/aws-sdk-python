"""Generated from Smithy shape ``com.amazonaws.glue#ComputeEnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.compute_environment

ComputeEnvironmentList: TypeAlias = list[
    "capo_glue.types.compute_environment.ComputeEnvironment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeEnvironmentList) -> list:
    import capo_glue.types.compute_environment

    out: list = []
    for item in value:
        out.append(capo_glue.types.compute_environment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComputeEnvironmentList:
    import capo_glue.types.compute_environment

    out: ComputeEnvironmentList = []
    for item in data:
        out.append(capo_glue.types.compute_environment.deserialize_aws_json_1_1(item))
    return out
