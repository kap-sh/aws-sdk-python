"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateIdNamespaceAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.generic_resource_name
    import aws_sdk_cleanrooms.types.id_mapping_config
    import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.tag_map


class CreateIdNamespaceAssociationInput(TypedDict, closed=True):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID namespace association.</p>"""
    input_reference_config: "aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig"
    """<p>The input reference configuration needed to create the ID namespace association.</p>"""
    tags: NotRequired["aws_sdk_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    name: "aws_sdk_cleanrooms.types.generic_resource_name.GenericResourceName"
    """<p>The name for the ID namespace association.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ID namespace association.</p>"""
    id_mapping_config: NotRequired[
        "aws_sdk_cleanrooms.types.id_mapping_config.IdMappingConfig"
    ]
    """<p>The configuration settings for the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdNamespaceAssociationInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config

    out["inputReferenceConfig"] = (
        aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config.serialize_json(
            value["input_reference_config"]
        )
    )
    if "tags" in value:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.serialize_json(value["tags"])
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "id_mapping_config" in value:
        import aws_sdk_cleanrooms.types.id_mapping_config

        out["idMappingConfig"] = (
            aws_sdk_cleanrooms.types.id_mapping_config.serialize_json(
                value["id_mapping_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateIdNamespaceAssociationInput:
    out: CreateIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
    if "inputReferenceConfig" in data:
        import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config

        out["input_reference_config"] = (
            aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdNamespaceAssociationInput.input_reference_config required"
        )
    if "tags" in data:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateIdNamespaceAssociationInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "idMappingConfig" in data:
        import aws_sdk_cleanrooms.types.id_mapping_config

        out["id_mapping_config"] = (
            aws_sdk_cleanrooms.types.id_mapping_config.deserialize_json(
                data["idMappingConfig"]
            )
        )
    return out
