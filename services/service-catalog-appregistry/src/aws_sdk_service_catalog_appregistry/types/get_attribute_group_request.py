"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetAttributeGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_specifier


class GetAttributeGroupRequest(TypedDict):
    attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier"
    """<p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAttributeGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAttributeGroupRequest:
    out: GetAttributeGroupRequest = {}  # type: ignore[typeddict-item]
    return out
