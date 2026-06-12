"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name
    import aws_sdk_clouddirectory.types.facet_attribute_definition
    import aws_sdk_clouddirectory.types.facet_attribute_reference
    import aws_sdk_clouddirectory.types.required_attribute_behavior


class FacetAttribute(TypedDict):
    name: "aws_sdk_clouddirectory.types.attribute_name.AttributeName"
    """<p>The name of the facet attribute.</p>"""
    attribute_definition: NotRequired[
        "aws_sdk_clouddirectory.types.facet_attribute_definition.FacetAttributeDefinition"
    ]
    """<p>A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html\">Attribute References</a> for more information.</p>"""
    attribute_reference: NotRequired[
        "aws_sdk_clouddirectory.types.facet_attribute_reference.FacetAttributeReference"
    ]
    """<p>An attribute reference that is associated with the attribute. See <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html\">Attribute References</a> for more information.</p>"""
    required_behavior: NotRequired[
        "aws_sdk_clouddirectory.types.required_attribute_behavior.RequiredAttributeBehavior"
    ]
    """<p>The required behavior of the <code>FacetAttribute</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FacetAttribute) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "attribute_definition" in value:
        import aws_sdk_clouddirectory.types.facet_attribute_definition

        out["AttributeDefinition"] = (
            aws_sdk_clouddirectory.types.facet_attribute_definition.serialize_json(
                value["attribute_definition"]
            )
        )
    if "attribute_reference" in value:
        import aws_sdk_clouddirectory.types.facet_attribute_reference

        out["AttributeReference"] = (
            aws_sdk_clouddirectory.types.facet_attribute_reference.serialize_json(
                value["attribute_reference"]
            )
        )
    if "required_behavior" in value:
        import aws_sdk_clouddirectory.types.required_attribute_behavior

        out["RequiredBehavior"] = (
            aws_sdk_clouddirectory.types.required_attribute_behavior.serialize_json(
                value["required_behavior"]
            )
        )
    return out


def deserialize_json(data: dict) -> FacetAttribute:
    out: FacetAttribute = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FacetAttribute.name required")
    if "AttributeDefinition" in data:
        import aws_sdk_clouddirectory.types.facet_attribute_definition

        out["attribute_definition"] = (
            aws_sdk_clouddirectory.types.facet_attribute_definition.deserialize_json(
                data["AttributeDefinition"]
            )
        )
    if "AttributeReference" in data:
        import aws_sdk_clouddirectory.types.facet_attribute_reference

        out["attribute_reference"] = (
            aws_sdk_clouddirectory.types.facet_attribute_reference.deserialize_json(
                data["AttributeReference"]
            )
        )
    if "RequiredBehavior" in data:
        import aws_sdk_clouddirectory.types.required_attribute_behavior

        out["required_behavior"] = (
            aws_sdk_clouddirectory.types.required_attribute_behavior.deserialize_json(
                data["RequiredBehavior"]
            )
        )
    return out
