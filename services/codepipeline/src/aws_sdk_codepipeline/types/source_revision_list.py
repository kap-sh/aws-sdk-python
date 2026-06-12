"""Generated from Smithy shape ``com.amazonaws.codepipeline#SourceRevisionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.source_revision

SourceRevisionList: TypeAlias = list[
    "aws_sdk_codepipeline.types.source_revision.SourceRevision"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceRevisionList) -> list:
    import aws_sdk_codepipeline.types.source_revision

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.source_revision.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SourceRevisionList:
    import aws_sdk_codepipeline.types.source_revision

    out: SourceRevisionList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.source_revision.deserialize_aws_json_1_1(item)
        )
    return out
