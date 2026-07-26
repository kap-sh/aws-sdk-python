"""Generated from Smithy shape ``com.amazonaws.codebuild#Builds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.build

Builds: TypeAlias = list["capo_codebuild.types.build.Build"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Builds) -> list:
    import capo_codebuild.types.build

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Builds:
    import capo_codebuild.types.build

    out: Builds = []
    for item in data:
        out.append(capo_codebuild.types.build.deserialize_aws_json_1_1(item))
    return out
