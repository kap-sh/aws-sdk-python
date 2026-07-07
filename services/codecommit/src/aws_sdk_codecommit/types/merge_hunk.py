"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeHunk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.is_hunk_conflict
    import aws_sdk_codecommit.types.merge_hunk_detail


class MergeHunk(TypedDict, closed=True):
    is_conflict: "aws_sdk_codecommit.types.is_hunk_conflict.IsHunkConflict"
    """<p>A Boolean value indicating whether a combination of hunks contains a conflict. Conflicts occur when the same file or the same lines in a file were modified in both the source and destination of a merge or pull request. Valid values include true, false, and null. True when the hunk represents a conflict and one or more files contains a line conflict. File mode conflicts in a merge do not set this to true.</p>"""
    source: NotRequired["aws_sdk_codecommit.types.merge_hunk_detail.MergeHunkDetail"]
    """<p>Information about the merge hunk in the source of a merge or pull request.</p>"""
    destination: NotRequired[
        "aws_sdk_codecommit.types.merge_hunk_detail.MergeHunkDetail"
    ]
    """<p>Information about the merge hunk in the destination of a merge or pull request.</p>"""
    base: NotRequired["aws_sdk_codecommit.types.merge_hunk_detail.MergeHunkDetail"]
    """<p>Information about the merge hunk in the base of a merge or pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeHunk) -> dict:
    out: dict = {}
    out["isConflict"] = value.get("is_conflict", False)
    if "source" in value:
        import aws_sdk_codecommit.types.merge_hunk_detail

        out["source"] = (
            aws_sdk_codecommit.types.merge_hunk_detail.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "destination" in value:
        import aws_sdk_codecommit.types.merge_hunk_detail

        out["destination"] = (
            aws_sdk_codecommit.types.merge_hunk_detail.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "base" in value:
        import aws_sdk_codecommit.types.merge_hunk_detail

        out["base"] = aws_sdk_codecommit.types.merge_hunk_detail.serialize_aws_json_1_1(
            value["base"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeHunk:
    out: MergeHunk = {}  # type: ignore[typeddict-item]
    if "isConflict" in data:
        out["is_conflict"] = data["isConflict"]
    else:
        out["is_conflict"] = False
    if "source" in data:
        import aws_sdk_codecommit.types.merge_hunk_detail

        out["source"] = (
            aws_sdk_codecommit.types.merge_hunk_detail.deserialize_aws_json_1_1(
                data["source"]
            )
        )
    if "destination" in data:
        import aws_sdk_codecommit.types.merge_hunk_detail

        out["destination"] = (
            aws_sdk_codecommit.types.merge_hunk_detail.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    if "base" in data:
        import aws_sdk_codecommit.types.merge_hunk_detail

        out["base"] = (
            aws_sdk_codecommit.types.merge_hunk_detail.deserialize_aws_json_1_1(
                data["base"]
            )
        )
    return out
