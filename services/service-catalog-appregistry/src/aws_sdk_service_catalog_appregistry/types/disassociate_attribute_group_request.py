"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#DisassociateAttributeGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_specifier
    import aws_sdk_service_catalog_appregistry.types.attribute_group_specifier


class DisassociateAttributeGroupRequest(TypedDict):
    application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p> The name, ID, or ARN of the application. </p>"""
    attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier"
    """<p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAttributeGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateAttributeGroupRequest:
    out: DisassociateAttributeGroupRequest = {}  # type: ignore[typeddict-item]
    return out
