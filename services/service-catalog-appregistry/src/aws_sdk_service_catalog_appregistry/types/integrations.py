"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#Integrations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.resource_group


class Integrations(TypedDict, closed=True):
    resource_group: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.resource_group.ResourceGroup"
    ]
    """<p> The information about the resource group integration.</p>"""
    application_tag_resource_group: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.resource_group.ResourceGroup"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Integrations) -> dict:
    out: dict = {}
    if "resource_group" in value:
        import aws_sdk_service_catalog_appregistry.types.resource_group

        out["resourceGroup"] = (
            aws_sdk_service_catalog_appregistry.types.resource_group.serialize_json(
                value["resource_group"]
            )
        )
    if "application_tag_resource_group" in value:
        import aws_sdk_service_catalog_appregistry.types.resource_group

        out["applicationTagResourceGroup"] = (
            aws_sdk_service_catalog_appregistry.types.resource_group.serialize_json(
                value["application_tag_resource_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> Integrations:
    out: Integrations = {}  # type: ignore[typeddict-item]
    if "resourceGroup" in data:
        import aws_sdk_service_catalog_appregistry.types.resource_group

        out["resource_group"] = (
            aws_sdk_service_catalog_appregistry.types.resource_group.deserialize_json(
                data["resourceGroup"]
            )
        )
    if "applicationTagResourceGroup" in data:
        import aws_sdk_service_catalog_appregistry.types.resource_group

        out["application_tag_resource_group"] = (
            aws_sdk_service_catalog_appregistry.types.resource_group.deserialize_json(
                data["applicationTagResourceGroup"]
            )
        )
    return out
