"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AssociateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_specifier
    import capo_service_catalog_appregistry.types.options
    import capo_service_catalog_appregistry.types.resource_specifier
    import capo_service_catalog_appregistry.types.resource_type


class AssociateResourceRequest(TypedDict, closed=True):
    application: "capo_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p> The name, ID, or ARN of the application. </p>"""
    resource_type: "capo_service_catalog_appregistry.types.resource_type.ResourceType"
    """<p>The type of resource of which the application will be associated.</p>"""
    resource: (
        "capo_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier"
    )
    """<p>The name or ID of the resource of which the application will be associated.</p>"""
    options: NotRequired["capo_service_catalog_appregistry.types.options.Options"]
    """<p> Determines whether an application tag is applied or skipped. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceRequest) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_service_catalog_appregistry.types.options

        out["options"] = capo_service_catalog_appregistry.types.options.serialize_json(
            value["options"]
        )
    return out


def deserialize_json(data: dict) -> AssociateResourceRequest:
    out: AssociateResourceRequest = {}  # type: ignore[typeddict-item]
    if "options" in data:
        import capo_service_catalog_appregistry.types.options

        out["options"] = (
            capo_service_catalog_appregistry.types.options.deserialize_json(
                data["options"]
            )
        )
    return out
