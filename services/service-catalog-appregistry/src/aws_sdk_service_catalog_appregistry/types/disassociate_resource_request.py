"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#DisassociateResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_specifier
    import aws_sdk_service_catalog_appregistry.types.resource_specifier
    import aws_sdk_service_catalog_appregistry.types.resource_type


class DisassociateResourceRequest(TypedDict):
    application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p>The name or ID of the application.</p>"""
    resource_type: (
        "aws_sdk_service_catalog_appregistry.types.resource_type.ResourceType"
    )
    """<p>The type of the resource that is being disassociated.</p>"""
    resource: (
        "aws_sdk_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier"
    )
    """<p>The name or ID of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateResourceRequest:
    out: DisassociateResourceRequest = {}  # type: ignore[typeddict-item]
    return out
