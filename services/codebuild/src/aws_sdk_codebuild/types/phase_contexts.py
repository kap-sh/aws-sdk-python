"""Generated from Smithy shape ``com.amazonaws.codebuild#PhaseContexts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.phase_context

PhaseContexts: TypeAlias = list["aws_sdk_codebuild.types.phase_context.PhaseContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhaseContexts) -> list:
    import aws_sdk_codebuild.types.phase_context

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.phase_context.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PhaseContexts:
    import aws_sdk_codebuild.types.phase_context

    out: PhaseContexts = []
    for item in data:
        out.append(aws_sdk_codebuild.types.phase_context.deserialize_aws_json_1_1(item))
    return out
