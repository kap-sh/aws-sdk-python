"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ApplicationTagResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_tag_status
    import aws_sdk_service_catalog_appregistry.types.next_token
    import aws_sdk_service_catalog_appregistry.types.resources_list
    import aws_sdk_service_catalog_appregistry.types.string


class ApplicationTagResult(TypedDict):
    application_tag_status: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_tag_status.ApplicationTagStatus"
    ]
    """<p> The application tag is in the process of being applied to a resource, was successfully applied to a resource, or failed to apply to a resource. </p>"""
    error_message: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.string.String"
    ]
    """<p> The message returned if the call fails. </p>"""
    resources: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.resources_list.ResourcesList"
    ]
    """<p> The resources associated with an application </p>"""
    next_token: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p> A unique pagination token for each page of results. Make the call again with the returned token to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationTagResult) -> dict:
    out: dict = {}
    if "application_tag_status" in value:
        import aws_sdk_service_catalog_appregistry.types.application_tag_status

        out["applicationTagStatus"] = (
            aws_sdk_service_catalog_appregistry.types.application_tag_status.serialize_json(
                value["application_tag_status"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "resources" in value:
        import aws_sdk_service_catalog_appregistry.types.resources_list

        out["resources"] = (
            aws_sdk_service_catalog_appregistry.types.resources_list.serialize_json(
                value["resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ApplicationTagResult:
    out: ApplicationTagResult = {}  # type: ignore[typeddict-item]
    if "applicationTagStatus" in data:
        import aws_sdk_service_catalog_appregistry.types.application_tag_status

        out["application_tag_status"] = (
            aws_sdk_service_catalog_appregistry.types.application_tag_status.deserialize_json(
                data["applicationTagStatus"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "resources" in data:
        import aws_sdk_service_catalog_appregistry.types.resources_list

        out["resources"] = (
            aws_sdk_service_catalog_appregistry.types.resources_list.deserialize_json(
                data["resources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
