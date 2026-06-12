"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#UpdateAttributeGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_specifier
    import aws_sdk_service_catalog_appregistry.types.attributes
    import aws_sdk_service_catalog_appregistry.types.description
    import aws_sdk_service_catalog_appregistry.types.name


class UpdateAttributeGroupRequest(TypedDict):
    attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier"
    """<p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>"""
    name: NotRequired["aws_sdk_service_catalog_appregistry.types.name.Name"]
    """<p>Deprecated: The new name of the attribute group. The name must be unique in the region in which you are updating the attribute group. Please do not use this field as we have stopped supporting name updates.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.description.Description"
    ]
    """<p>The description of the attribute group that the user provides.</p>"""
    attributes: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attributes.Attributes"
    ]
    """<p>A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttributeGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "attributes" in value:
        out["attributes"] = value["attributes"]
    return out


def deserialize_json(data: dict) -> UpdateAttributeGroupRequest:
    out: UpdateAttributeGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "attributes" in data:
        out["attributes"] = data["attributes"]
    return out
