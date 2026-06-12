"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeFolderContentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.field_names_type
    import aws_sdk_workdocs.types.folder_content_type
    import aws_sdk_workdocs.types.limit_type
    import aws_sdk_workdocs.types.order_type
    import aws_sdk_workdocs.types.page_marker_type
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.resource_sort_type


class DescribeFolderContentsRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the folder.</p>"""
    sort: NotRequired["aws_sdk_workdocs.types.resource_sort_type.ResourceSortType"]
    """<p>The sorting criteria.</p>"""
    order: NotRequired["aws_sdk_workdocs.types.order_type.OrderType"]
    """<p>The order for the contents of the folder.</p>"""
    limit: NotRequired["aws_sdk_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of items to return with this call.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. This marker was received from a previous call.</p>"""
    type: NotRequired["aws_sdk_workdocs.types.folder_content_type.FolderContentType"]
    """<p>The type of items.</p>"""
    include: NotRequired["aws_sdk_workdocs.types.field_names_type.FieldNamesType"]
    """<p>The contents to include. Specify \"INITIALIZED\" to include initialized documents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFolderContentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFolderContentsRequest:
    out: DescribeFolderContentsRequest = {}  # type: ignore[typeddict-item]
    return out
