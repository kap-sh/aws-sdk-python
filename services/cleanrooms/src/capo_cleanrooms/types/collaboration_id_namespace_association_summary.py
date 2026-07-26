"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationIdNamespaceAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.generic_resource_name
    import capo_cleanrooms.types.id_namespace_association_arn
    import capo_cleanrooms.types.id_namespace_association_identifier
    import capo_cleanrooms.types.id_namespace_association_input_reference_config
    import capo_cleanrooms.types.id_namespace_association_input_reference_properties_summary
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.uuid


class CollaborationIdNamespaceAssociationSummary(TypedDict, closed=True):
    arn: "capo_cleanrooms.types.id_namespace_association_arn.IdNamespaceAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration ID namespace association.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the collaboration ID namespace association was created.</p>"""
    id: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier"
    """<p>The unique identifier of the collaboration ID namespace association.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the collaboration ID namespace association was updated.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains this collaboration ID namespace association.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this collaboration ID namespace association.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account that created this collaboration ID namespace association.</p>"""
    input_reference_config: "capo_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig"
    """<p>The input reference configuration that's used to create the collaboration ID namespace association.</p>"""
    name: "capo_cleanrooms.types.generic_resource_name.GenericResourceName"
    """<p>The name of the collaboration ID namespace association.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the collaboration ID namepsace association.</p>"""
    input_reference_properties: "capo_cleanrooms.types.id_namespace_association_input_reference_properties_summary.IdNamespaceAssociationInputReferencePropertiesSummary"
    """<p>The input reference properties that are used to create the collaboration ID namespace association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationIdNamespaceAssociationSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    out["id"] = value["id"]
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["creatorAccountId"] = value["creator_account_id"]
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


def deserialize_json(data: dict) -> CollaborationIdNamespaceAssociationSummary:
    out: CollaborationIdNamespaceAssociationSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.arn required"
        )
    if "createTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.create_time required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.id required"
        )
    if "updateTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.update_time required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.collaboration_arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.collaboration_id required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.creator_account_id required"
        )
    if "inputReferenceConfig" in data:
        import capo_cleanrooms.types.id_namespace_association_input_reference_config

        out["input_reference_config"] = (
            capo_cleanrooms.types.id_namespace_association_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.input_reference_config required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CollaborationIdNamespaceAssociationSummary.name required"
        )
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
            "CollaborationIdNamespaceAssociationSummary.input_reference_properties required"
        )
    return out
