"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AssociateAttributeGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_specifier
    import aws_sdk_service_catalog_appregistry.types.attribute_group_specifier


class AssociateAttributeGroupRequest(TypedDict, closed=True):
    application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p> The name, ID, or ARN of the application. </p>"""
    attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier"
    """<p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAttributeGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateAttributeGroupRequest:
    out: AssociateAttributeGroupRequest = {}  # type: ignore[typeddict-item]
    return out
