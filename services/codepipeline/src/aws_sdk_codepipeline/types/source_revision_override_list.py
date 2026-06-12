"""Generated from Smithy shape ``com.amazonaws.codepipeline#SourceRevisionOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.source_revision_override

SourceRevisionOverrideList: TypeAlias = list[
    "aws_sdk_codepipeline.types.source_revision_override.SourceRevisionOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceRevisionOverrideList) -> list:
    import aws_sdk_codepipeline.types.source_revision_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.source_revision_override.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SourceRevisionOverrideList:
    import aws_sdk_codepipeline.types.source_revision_override

    out: SourceRevisionOverrideList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.source_revision_override.deserialize_aws_json_1_1(
                item
            )
        )
    return out
