"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildPhases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.build_phase

BuildPhases: TypeAlias = list["capo_codebuild.types.build_phase.BuildPhase"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildPhases) -> list:
    import capo_codebuild.types.build_phase

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_phase.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildPhases:
    import capo_codebuild.types.build_phase

    out: BuildPhases = []
    for item in data:
        out.append(capo_codebuild.types.build_phase.deserialize_aws_json_1_1(item))
    return out
