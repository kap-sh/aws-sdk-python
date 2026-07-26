"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetAssociatedResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_specifier
    import capo_service_catalog_appregistry.types.get_associated_resource_filter
    import capo_service_catalog_appregistry.types.max_results
    import capo_service_catalog_appregistry.types.next_token
    import capo_service_catalog_appregistry.types.resource_specifier
    import capo_service_catalog_appregistry.types.resource_type


class GetAssociatedResourceRequest(TypedDict, closed=True):
    application: "capo_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p> The name, ID, or ARN of the application. </p>"""
    resource_type: "capo_service_catalog_appregistry.types.resource_type.ResourceType"
    """<p>The type of resource associated with the application.</p>"""
    resource: (
        "capo_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier"
    )
    """<p>The name or ID of the resource associated with the application.</p>"""
    next_token: NotRequired[
        "capo_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p> A unique pagination token for each page of results. Make the call again with the returned token to retrieve the next page of results. </p>"""
    resource_tag_status: NotRequired[
        "capo_service_catalog_appregistry.types.get_associated_resource_filter.GetAssociatedResourceFilter"
    ]
    """<p> States whether an application tag is applied, not applied, in the process of being applied, or skipped. </p>"""
    max_results: NotRequired[
        "capo_service_catalog_appregistry.types.max_results.MaxResults"
    ]
    """<p> The maximum number of results to return. If the parameter is omitted, it defaults to 25. The value is optional. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssociatedResourceRequest:
    out: GetAssociatedResourceRequest = {}  # type: ignore[typeddict-item]
    return out
