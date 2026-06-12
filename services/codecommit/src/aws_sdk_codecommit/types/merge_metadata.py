"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.is_merged
    import aws_sdk_codecommit.types.merge_option_type_enum


class MergeMetadata(TypedDict):
    is_merged: "aws_sdk_codecommit.types.is_merged.IsMerged"
    """<p>A Boolean value indicating whether the merge has been made.</p>"""
    merged_by: NotRequired["aws_sdk_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user who merged the branches.</p>"""
    merge_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The commit ID for the merge commit, if any.</p>"""
    merge_option: NotRequired[
        "aws_sdk_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum"
    ]
    """<p>The merge strategy used in the merge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeMetadata) -> dict:
    out: dict = {}
    out["isMerged"] = value.get("is_merged", False)
    if "merged_by" in value:
        out["mergedBy"] = value["merged_by"]
    if "merge_commit_id" in value:
        out["mergeCommitId"] = value["merge_commit_id"]
    if "merge_option" in value:
        import aws_sdk_codecommit.types.merge_option_type_enum

        out["mergeOption"] = (
            aws_sdk_codecommit.types.merge_option_type_enum.serialize_aws_json_1_1(
                value["merge_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeMetadata:
    out: MergeMetadata = {}  # type: ignore[typeddict-item]
    if "isMerged" in data:
        out["is_merged"] = data["isMerged"]
    else:
        out["is_merged"] = False
    if "mergedBy" in data:
        out["merged_by"] = data["mergedBy"]
    if "mergeCommitId" in data:
        out["merge_commit_id"] = data["mergeCommitId"]
    if "mergeOption" in data:
        import aws_sdk_codecommit.types.merge_option_type_enum

        out["merge_option"] = (
            aws_sdk_codecommit.types.merge_option_type_enum.deserialize_aws_json_1_1(
                data["mergeOption"]
            )
        )
    return out
