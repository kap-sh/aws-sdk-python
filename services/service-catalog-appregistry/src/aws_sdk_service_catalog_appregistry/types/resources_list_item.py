"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourcesListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.arn
    import aws_sdk_service_catalog_appregistry.types.resource_item_type
    import aws_sdk_service_catalog_appregistry.types.resources_list_item_error_message
    import aws_sdk_service_catalog_appregistry.types.string


class ResourcesListItem(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_service_catalog_appregistry.types.arn.Arn"]
    """<p> The Amazon resource name (ARN) of the resource. </p>"""
    error_message: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.resources_list_item_error_message.ResourcesListItemErrorMessage"
    ]
    """<p> The message returned if the call fails. </p>"""
    status: NotRequired["aws_sdk_service_catalog_appregistry.types.string.String"]
    """<p> The status of the list item. </p>"""
    resource_type: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.resource_item_type.ResourceItemType"
    ]
    """<p> Provides information about the AppRegistry resource type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesListItem) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "status" in value:
        out["status"] = value["status"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourcesListItem:
    out: ResourcesListItem = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "status" in data:
        out["status"] = data["status"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out
