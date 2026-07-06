"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.max_results
    import aws_sdk_service_catalog_appregistry.types.next_token


class ListApplicationsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call. </p>"""
    max_results: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
    ]
    """<p>The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
