"""Generated from Smithy shape ``com.amazonaws.glue#ComputeEnvironments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.compute_environment

ComputeEnvironments: TypeAlias = list[
    "aws_sdk_glue.types.compute_environment.ComputeEnvironment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeEnvironments) -> list:
    import aws_sdk_glue.types.compute_environment

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.compute_environment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComputeEnvironments:
    import aws_sdk_glue.types.compute_environment

    out: ComputeEnvironments = []
    for item in data:
        out.append(
            aws_sdk_glue.types.compute_environment.deserialize_aws_json_1_1(item)
        )
    return out
