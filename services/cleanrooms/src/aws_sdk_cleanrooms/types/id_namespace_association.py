"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdNamespaceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.generic_resource_name
    import aws_sdk_cleanrooms.types.id_mapping_config
    import aws_sdk_cleanrooms.types.id_namespace_association_arn
    import aws_sdk_cleanrooms.types.id_namespace_association_identifier
    import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config
    import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_properties
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class IdNamespaceAssociation(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier"
    """<p>The unique identifier for this ID namespace association.</p>"""
    arn: "aws_sdk_cleanrooms.types.id_namespace_association_arn.IdNamespaceAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the ID namespace association.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the membership resource for this ID namespace association.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership resource for this ID namespace association.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this ID namespace association.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains this ID namespace association.</p>"""
    name: "aws_sdk_cleanrooms.types.generic_resource_name.GenericResourceName"
    """<p>The name of this ID namespace association.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ID namespace association.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the ID namespace association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ID namespace association was updated.</p>"""
    input_reference_config: "aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig"
    """<p>The input reference configuration for the ID namespace association.</p>"""
    input_reference_properties: "aws_sdk_cleanrooms.types.id_namespace_association_input_reference_properties.IdNamespaceAssociationInputReferenceProperties"
    """<p>The input reference properties for the ID namespace association.</p>"""
    id_mapping_config: NotRequired[
        "aws_sdk_cleanrooms.types.id_mapping_config.IdMappingConfig"
    ]
    """<p>The configuration settings for the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceAssociation) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config

    out["inputReferenceConfig"] = (
        aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config.serialize_json(
            value["input_reference_config"]
        )
    )
    import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_properties

    out["inputReferenceProperties"] = (
        aws_sdk_cleanrooms.types.id_namespace_association_input_reference_properties.serialize_json(
            value["input_reference_properties"]
        )
    )
    if "id_mapping_config" in value:
        import aws_sdk_cleanrooms.types.id_mapping_config

        out["idMappingConfig"] = (
            aws_sdk_cleanrooms.types.id_mapping_config.serialize_json(
                value["id_mapping_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> IdNamespaceAssociation:
    out: IdNamespaceAssociation = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("IdNamespaceAssociation.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IdNamespaceAssociation.arn required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("IdNamespaceAssociation.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("IdNamespaceAssociation.membership_arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("IdNamespaceAssociation.collaboration_id required")
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("IdNamespaceAssociation.collaboration_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IdNamespaceAssociation.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("IdNamespaceAssociation.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("IdNamespaceAssociation.update_time required")
    if "inputReferenceConfig" in data:
        import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config

        out["input_reference_config"] = (
            aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "IdNamespaceAssociation.input_reference_config required"
        )
    if "inputReferenceProperties" in data:
        import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_properties

        out["input_reference_properties"] = (
            aws_sdk_cleanrooms.types.id_namespace_association_input_reference_properties.deserialize_json(
                data["inputReferenceProperties"]
            )
        )
    else:
        raise DeserializationError(
            "IdNamespaceAssociation.input_reference_properties required"
        )
    if "idMappingConfig" in data:
        import aws_sdk_cleanrooms.types.id_mapping_config

        out["id_mapping_config"] = (
            aws_sdk_cleanrooms.types.id_mapping_config.deserialize_json(
                data["idMappingConfig"]
            )
        )
    return out
