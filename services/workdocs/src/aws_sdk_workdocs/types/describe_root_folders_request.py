"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeRootFoldersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.limit_type
    import aws_sdk_workdocs.types.page_marker_type


class DescribeRootFoldersRequest(TypedDict):
    authentication_token: (
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    )
    """<p>Amazon WorkDocs authentication token.</p>"""
    limit: NotRequired["aws_sdk_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of items to return.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRootFoldersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRootFoldersRequest:
    out: DescribeRootFoldersRequest = {}  # type: ignore[typeddict-item]
    return out
