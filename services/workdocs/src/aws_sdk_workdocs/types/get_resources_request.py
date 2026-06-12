"""Generated from Smithy shape ``com.amazonaws.workdocs#GetResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.limit_type
    import aws_sdk_workdocs.types.page_marker_type
    import aws_sdk_workdocs.types.resource_collection_type


class GetResourcesRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>The Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    user_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The user ID for the resource collection. This is a required field for accessing the API operation using IAM credentials.</p>"""
    collection_type: NotRequired[
        "aws_sdk_workdocs.types.resource_collection_type.ResourceCollectionType"
    ]
    """<p>The collection type.</p>"""
    limit: NotRequired["aws_sdk_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of resources to return.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. This marker was received from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcesRequest:
    out: GetResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
