"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.arn
    import capo_service_catalog_appregistry.types.options
    import capo_service_catalog_appregistry.types.resource_details
    import capo_service_catalog_appregistry.types.resource_specifier
    import capo_service_catalog_appregistry.types.resource_type


class ResourceInfo(TypedDict, closed=True):
    name: NotRequired[
        "capo_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier"
    ]
    """<p>The name of the resource.</p>"""
    arn: NotRequired["capo_service_catalog_appregistry.types.arn.Arn"]
    """<p>The Amazon resource name (ARN) that specifies the resource across services.</p>"""
    resource_type: NotRequired[
        "capo_service_catalog_appregistry.types.resource_type.ResourceType"
    ]
    """<p> Provides information about the Service Catalog App Registry resource type. </p>"""
    resource_details: NotRequired[
        "capo_service_catalog_appregistry.types.resource_details.ResourceDetails"
    ]
    """<p> The details related to the resource. </p>"""
    options: NotRequired["capo_service_catalog_appregistry.types.options.Options"]
    """<p> Determines whether an application tag is applied or skipped. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "resource_type" in value:
        import capo_service_catalog_appregistry.types.resource_type

        out["resourceType"] = (
            capo_service_catalog_appregistry.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "resource_details" in value:
        import capo_service_catalog_appregistry.types.resource_details

        out["resourceDetails"] = (
            capo_service_catalog_appregistry.types.resource_details.serialize_json(
                value["resource_details"]
            )
        )
    if "options" in value:
        import capo_service_catalog_appregistry.types.options

        out["options"] = capo_service_catalog_appregistry.types.options.serialize_json(
            value["options"]
        )
    return out


def deserialize_json(data: dict) -> ResourceInfo:
    out: ResourceInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "resourceType" in data:
        import capo_service_catalog_appregistry.types.resource_type

        out["resource_type"] = (
            capo_service_catalog_appregistry.types.resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if "resourceDetails" in data:
        import capo_service_catalog_appregistry.types.resource_details

        out["resource_details"] = (
            capo_service_catalog_appregistry.types.resource_details.deserialize_json(
                data["resourceDetails"]
            )
        )
    if "options" in data:
        import capo_service_catalog_appregistry.types.options

        out["options"] = (
            capo_service_catalog_appregistry.types.options.deserialize_json(
                data["options"]
            )
        )
    return out
