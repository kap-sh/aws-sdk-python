"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListAssociatedResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.next_token
    import aws_sdk_service_catalog_appregistry.types.resources


class ListAssociatedResourcesResponse(TypedDict, closed=True):
    resources: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.resources.Resources"
    ]
    """<p>Information about the resources.</p>"""
    next_token: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedResourcesResponse) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_service_catalog_appregistry.types.resources

        out["resources"] = (
            aws_sdk_service_catalog_appregistry.types.resources.serialize_json(
                value["resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedResourcesResponse:
    out: ListAssociatedResourcesResponse = {}  # type: ignore[typeddict-item]
    if "resources" in data:
        import aws_sdk_service_catalog_appregistry.types.resources

        out["resources"] = (
            aws_sdk_service_catalog_appregistry.types.resources.deserialize_json(
                data["resources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
