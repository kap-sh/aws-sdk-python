"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListAttributeGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.max_results
    import aws_sdk_service_catalog_appregistry.types.next_token


class ListAttributeGroupsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call. </p>"""
    max_results: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
    ]
    """<p>The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttributeGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAttributeGroupsRequest:
    out: ListAttributeGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
