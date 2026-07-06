"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkFacet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name_list
    import aws_sdk_clouddirectory.types.typed_link_attribute_definition_list
    import aws_sdk_clouddirectory.types.typed_link_name


class TypedLinkFacet(TypedDict, closed=True):
    name: "aws_sdk_clouddirectory.types.typed_link_name.TypedLinkName"
    """<p>The unique name of the typed link facet.</p>"""
    attributes: "aws_sdk_clouddirectory.types.typed_link_attribute_definition_list.TypedLinkAttributeDefinitionList"
    """<p>A set of key-value pairs associated with the typed link. Typed link attributes are used when you have data values that are related to the link itself, and not to one of the two objects being linked. Identity attributes also serve to distinguish the link from others of the same type between the same objects.</p>"""
    identity_attribute_order: (
        "aws_sdk_clouddirectory.types.attribute_name_list.AttributeNameList"
    )
    """<p>The set of attributes that distinguish links made from this facet from each other, in the order of significance. Listing typed links can filter on the values of these attributes. See <a>ListOutgoingTypedLinks</a> and <a>ListIncomingTypedLinks</a> for details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkFacet) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_clouddirectory.types.typed_link_attribute_definition_list

    out["Attributes"] = (
        aws_sdk_clouddirectory.types.typed_link_attribute_definition_list.serialize_json(
            value["attributes"]
        )
    )
    import aws_sdk_clouddirectory.types.attribute_name_list

    out["IdentityAttributeOrder"] = (
        aws_sdk_clouddirectory.types.attribute_name_list.serialize_json(
            value["identity_attribute_order"]
        )
    )
    return out


def deserialize_json(data: dict) -> TypedLinkFacet:
    out: TypedLinkFacet = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("TypedLinkFacet.name required")
    if "Attributes" in data:
        import aws_sdk_clouddirectory.types.typed_link_attribute_definition_list

        out["attributes"] = (
            aws_sdk_clouddirectory.types.typed_link_attribute_definition_list.deserialize_json(
                data["Attributes"]
            )
        )
    else:
        raise DeserializationError("TypedLinkFacet.attributes required")
    if "IdentityAttributeOrder" in data:
        import aws_sdk_clouddirectory.types.attribute_name_list

        out["identity_attribute_order"] = (
            aws_sdk_clouddirectory.types.attribute_name_list.deserialize_json(
                data["IdentityAttributeOrder"]
            )
        )
    else:
        raise DeserializationError("TypedLinkFacet.identity_attribute_order required")
    return out
