"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeCommentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.document_version_id_type
    import aws_sdk_workdocs.types.limit_type
    import aws_sdk_workdocs.types.marker_type
    import aws_sdk_workdocs.types.resource_id_type


class DescribeCommentsRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType"
    """<p>The ID of the document version.</p>"""
    limit: NotRequired["aws_sdk_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of items to return.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.marker_type.MarkerType"]
    """<p>The marker for the next set of results. This marker was received from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCommentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCommentsRequest:
    out: DescribeCommentsRequest = {}  # type: ignore[typeddict-item]
    return out
