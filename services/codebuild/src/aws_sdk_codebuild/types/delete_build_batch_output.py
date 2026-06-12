"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteBuildBatchOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_ids
    import aws_sdk_codebuild.types.builds_not_deleted
    import aws_sdk_codebuild.types.string


class DeleteBuildBatchOutput(TypedDict):
    status_code: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The status code.</p>"""
    builds_deleted: NotRequired["aws_sdk_codebuild.types.build_ids.BuildIds"]
    """<p>An array of strings that contain the identifiers of the builds that were deleted.</p>"""
    builds_not_deleted: NotRequired[
        "aws_sdk_codebuild.types.builds_not_deleted.BuildsNotDeleted"
    ]
    """<p>An array of <code>BuildNotDeleted</code> objects that specify the builds that could not be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBuildBatchOutput) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
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


def deserialize_aws_json_1_1(data: dict) -> DeleteBuildBatchOutput:
    out: DeleteBuildBatchOutput = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
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
