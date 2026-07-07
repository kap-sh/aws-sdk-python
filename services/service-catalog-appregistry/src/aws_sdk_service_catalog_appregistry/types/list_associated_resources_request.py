"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListAssociatedResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_specifier
    import aws_sdk_service_catalog_appregistry.types.max_results
    import aws_sdk_service_catalog_appregistry.types.next_token


class ListAssociatedResourcesRequest(TypedDict, closed=True):
    application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p> The name, ID, or ARN of the application. </p>"""
    next_token: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call. </p>"""
    max_results: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
    ]
    """<p>The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociatedResourcesRequest:
    out: ListAssociatedResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
