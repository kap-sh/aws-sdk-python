"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeCommentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.comment_list
    import aws_sdk_workdocs.types.marker_type


class DescribeCommentsResponse(TypedDict, closed=True):
    comments: NotRequired["aws_sdk_workdocs.types.comment_list.CommentList"]
    """<p>The list of comments for the specified document version.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.marker_type.MarkerType"]
    """<p>The marker for the next set of results. This marker was received from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCommentsResponse) -> dict:
    out: dict = {}
    if "comments" in value:
        import aws_sdk_workdocs.types.comment_list

        out["Comments"] = aws_sdk_workdocs.types.comment_list.serialize_json(
            value["comments"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeCommentsResponse:
    out: DescribeCommentsResponse = {}  # type: ignore[typeddict-item]
    if "Comments" in data:
        import aws_sdk_workdocs.types.comment_list

        out["comments"] = aws_sdk_workdocs.types.comment_list.deserialize_json(
            data["Comments"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
