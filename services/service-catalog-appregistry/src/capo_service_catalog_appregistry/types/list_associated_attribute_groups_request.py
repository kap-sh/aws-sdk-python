"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListAssociatedAttributeGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_specifier
    import capo_service_catalog_appregistry.types.max_results
    import capo_service_catalog_appregistry.types.next_token


class ListAssociatedAttributeGroupsRequest(TypedDict, closed=True):
    application: "capo_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p>The name or ID of the application.</p>"""
    next_token: NotRequired[
        "capo_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call. </p>"""
    max_results: NotRequired[
        "capo_service_catalog_appregistry.types.max_results.MaxResults"
    ]
    """<p>The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedAttributeGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociatedAttributeGroupsRequest:
    out: ListAssociatedAttributeGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
