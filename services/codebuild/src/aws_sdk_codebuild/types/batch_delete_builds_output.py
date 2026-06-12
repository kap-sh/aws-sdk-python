"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchDeleteBuildsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_ids
    import aws_sdk_codebuild.types.builds_not_deleted


class BatchDeleteBuildsOutput(TypedDict):
    builds_deleted: NotRequired["aws_sdk_codebuild.types.build_ids.BuildIds"]
    """<p>The IDs of the builds that were successfully deleted.</p>"""
    builds_not_deleted: NotRequired[
        "aws_sdk_codebuild.types.builds_not_deleted.BuildsNotDeleted"
    ]
    """<p>Information about any builds that could not be successfully deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteBuildsOutput) -> dict:
    out: dict = {}
    if "builds_deleted" in value:
        import aws_sdk_codebuild.types.build_ids

        out["buildsDeleted"] = aws_sdk_codebuild.types.build_ids.serialize_aws_json_1_1(
            value["builds_deleted"]
        )
    if "builds_not_deleted" in value:
        import aws_sdk_codebuild.types.builds_not_deleted

        out["buildsNotDeleted"] = (
            aws_sdk_codebuild.types.builds_not_deleted.serialize_aws_json_1_1(
                value["builds_not_deleted"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteBuildsOutput:
    out: BatchDeleteBuildsOutput = {}  # type: ignore[typeddict-item]
    if "buildsDeleted" in data:
        import aws_sdk_codebuild.types.build_ids

        out["builds_deleted"] = (
            aws_sdk_codebuild.types.build_ids.deserialize_aws_json_1_1(
                data["buildsDeleted"]
            )
        )
    if "buildsNotDeleted" in data:
        import aws_sdk_codebuild.types.builds_not_deleted

        out["builds_not_deleted"] = (
            aws_sdk_codebuild.types.builds_not_deleted.deserialize_aws_json_1_1(
                data["buildsNotDeleted"]
            )
        )
    return out
