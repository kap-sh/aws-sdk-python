"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AssociateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_specifier
    import aws_sdk_service_catalog_appregistry.types.options
    import aws_sdk_service_catalog_appregistry.types.resource_specifier
    import aws_sdk_service_catalog_appregistry.types.resource_type


class AssociateResourceRequest(TypedDict, closed=True):
    application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p> The name, ID, or ARN of the application. </p>"""
    resource_type: (
        "aws_sdk_service_catalog_appregistry.types.resource_type.ResourceType"
    )
    """<p>The type of resource of which the application will be associated.</p>"""
    resource: (
        "aws_sdk_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier"
    )
    """<p>The name or ID of the resource of which the application will be associated.</p>"""
    options: NotRequired["aws_sdk_service_catalog_appregistry.types.options.Options"]
    """<p> Determines whether an application tag is applied or skipped. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceRequest) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_service_catalog_appregistry.types.options

        out["options"] = (
            aws_sdk_service_catalog_appregistry.types.options.serialize_json(
                value["options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateResourceRequest:
    out: AssociateResourceRequest = {}  # type: ignore[typeddict-item]
    if "options" in data:
        import aws_sdk_service_catalog_appregistry.types.options

        out["options"] = (
            aws_sdk_service_catalog_appregistry.types.options.deserialize_json(
                data["options"]
            )
        )
    return out
