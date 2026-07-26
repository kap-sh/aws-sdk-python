"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdNamespaceAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.generic_resource_name
    import capo_cleanrooms.types.id_namespace_association_arn
    import capo_cleanrooms.types.id_namespace_association_input_reference_config
    import capo_cleanrooms.types.id_namespace_association_input_reference_properties_summary
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.uuid


class IdNamespaceAssociationSummary(TypedDict, closed=True):
    membership_id: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>The unique identifier of the membership resource for this ID namespace association.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership resource for this ID namespace association.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains this ID namespace association.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this ID namespace association.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which this ID namespace association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which this ID namespace association has been updated.</p>"""
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of this ID namespace association.</p>"""
    arn: "capo_cleanrooms.types.id_namespace_association_arn.IdNamespaceAssociationArn"
    """<p>The Amazon Resource Name (ARN) of this ID namespace association.</p>"""
    input_reference_config: "capo_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig"
    """<p>The input reference configuration details for this ID namespace association.</p>"""
    name: "capo_cleanrooms.types.generic_resource_name.GenericResourceName"
    """<p>The name of the ID namespace association.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ID namespace association.</p>"""
    input_reference_properties: "capo_cleanrooms.types.id_namespace_association_input_reference_properties_summary.IdNamespaceAssociationInputReferencePropertiesSummary"
    """<p>The input reference properties for this ID namespace association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceAssociationSummary) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_cleanrooms.types.id_namespace_association_input_reference_config

    out["inputReferenceConfig"] = (
        capo_cleanrooms.types.id_namespace_association_input_reference_config.serialize_json(
            value["input_reference_config"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanrooms.types.id_namespace_association_input_reference_properties_summary

    out["inputReferenceProperties"] = (
        capo_cleanrooms.types.id_namespace_association_input_reference_properties_summary.serialize_json(
            value["input_reference_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> IdNamespaceAssociationSummary:
    out: IdNamespaceAssociationSummary = {}  # type: ignore[typeddict-item]
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError(
            "IdNamespaceAssociationSummary.membership_id required"
        )
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError(
            "IdNamespaceAssociationSummary.membership_arn required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "IdNamespaceAssociationSummary.collaboration_arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "IdNamespaceAssociationSummary.collaboration_id required"
        )
    if "createTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("IdNamespaceAssociationSummary.create_time required")
    if "updateTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("IdNamespaceAssociationSummary.update_time required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("IdNamespaceAssociationSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IdNamespaceAssociationSummary.arn required")
    if "inputReferenceConfig" in data:
        import capo_cleanrooms.types.id_namespace_association_input_reference_config

        out["input_reference_config"] = (
            capo_cleanrooms.types.id_namespace_association_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "IdNamespaceAssociationSummary.input_reference_config required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IdNamespaceAssociationSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "inputReferenceProperties" in data:
        import capo_cleanrooms.types.id_namespace_association_input_reference_properties_summary

        out["input_reference_properties"] = (
            capo_cleanrooms.types.id_namespace_association_input_reference_properties_summary.deserialize_json(
                data["inputReferenceProperties"]
            )
        )
    else:
        raise DeserializationError(
            "IdNamespaceAssociationSummary.input_reference_properties required"
        )
    return out
