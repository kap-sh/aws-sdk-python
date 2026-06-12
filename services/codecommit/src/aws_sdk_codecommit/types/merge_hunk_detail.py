"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeHunkDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.hunk_content
    import aws_sdk_codecommit.types.line_number


class MergeHunkDetail(TypedDict):
    start_line: NotRequired["aws_sdk_codecommit.types.line_number.LineNumber"]
    """<p>The start position of the hunk in the merge result.</p>"""
    end_line: NotRequired["aws_sdk_codecommit.types.line_number.LineNumber"]
    """<p>The end position of the hunk in the merge result.</p>"""
    hunk_content: NotRequired["aws_sdk_codecommit.types.hunk_content.HunkContent"]
    """<p>The base-64 encoded content of the hunk merged region that might contain a conflict.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeHunkDetail) -> dict:
    out: dict = {}
    if "start_line" in value:
        out["startLine"] = value["start_line"]
    if "end_line" in value:
        out["endLine"] = value["end_line"]
    if "hunk_content" in value:
        out["hunkContent"] = value["hunk_content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeHunkDetail:
    out: MergeHunkDetail = {}  # type: ignore[typeddict-item]
    if "startLine" in data:
        out["start_line"] = data["startLine"]
    if "endLine" in data:
        out["end_line"] = data["endLine"]
    if "hunkContent" in data:
        out["hunk_content"] = data["hunkContent"]
    return out
