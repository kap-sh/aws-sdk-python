"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIdNamespaceAssociationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.generic_resource_name
    import aws_sdk_cleanrooms.types.id_mapping_config
    import aws_sdk_cleanrooms.types.id_namespace_association_identifier
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.resource_description


class UpdateIdNamespaceAssociationInput(TypedDict):
    id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier"
    """<p>The unique identifier of the ID namespace association that you want to update.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID namespace association that you want to update.</p>"""
    name: NotRequired[
        "aws_sdk_cleanrooms.types.generic_resource_name.GenericResourceName"
    ]
    """<p>A new name for the ID namespace association.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>A new description for the ID namespace association.</p>"""
    id_mapping_config: NotRequired[
        "aws_sdk_cleanrooms.types.id_mapping_config.IdMappingConfig"
    ]
    """<p>The configuration settings for the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdNamespaceAssociationInput) -> dict:
    out: dict = {}
    if "name" in value:
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


def deserialize_json(data: dict) -> UpdateIdNamespaceAssociationInput:
    out: UpdateIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
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
