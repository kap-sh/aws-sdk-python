"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListAttributeGroupsForApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_specifier
    import aws_sdk_service_catalog_appregistry.types.max_results
    import aws_sdk_service_catalog_appregistry.types.next_token


class ListAttributeGroupsForApplicationRequest(TypedDict):
    application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p>The name or ID of the application.</p>"""
    next_token: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>This token retrieves the next page of results after a previous API call.</p>"""
    max_results: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
    ]
    """<p>The upper bound of the number of results to return. The value cannot exceed 25. If you omit this parameter, it defaults to 25. This value is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttributeGroupsForApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAttributeGroupsForApplicationRequest:
    out: ListAttributeGroupsForApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
