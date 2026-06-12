"""Generated from Smithy shape ``com.amazonaws.codebuild#SandboxSessionPhases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.sandbox_session_phase

SandboxSessionPhases: TypeAlias = list[
    "aws_sdk_codebuild.types.sandbox_session_phase.SandboxSessionPhase"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SandboxSessionPhases) -> list:
    import aws_sdk_codebuild.types.sandbox_session_phase

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.sandbox_session_phase.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SandboxSessionPhases:
    import aws_sdk_codebuild.types.sandbox_session_phase

    out: SandboxSessionPhases = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.sandbox_session_phase.deserialize_aws_json_1_1(item)
        )
    return out
