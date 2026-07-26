"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredAudienceModelAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.configured_audience_model_arn
    import capo_cleanrooms.types.configured_audience_model_association_arn
    import capo_cleanrooms.types.configured_audience_model_association_identifier
    import capo_cleanrooms.types.configured_audience_model_association_name
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.uuid


class ConfiguredAudienceModelAssociation(TypedDict, closed=True):
    id: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier"
    """<p>A unique identifier of the configured audience model association.</p>"""
    arn: "capo_cleanrooms.types.configured_audience_model_association_arn.ConfiguredAudienceModelAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model association.</p>"""
    configured_audience_model_arn: (
        "capo_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the configured audience model that was used for this configured audience model association.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier for the membership that contains this configured audience model association.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership that contains this configured audience model association.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier of the collaboration that contains this configured audience model association.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains this configured audience model association.</p>"""
    name: "capo_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
    """<p>The name of the configured audience model association.</p>"""
    manage_resource_policies: "bool"
    """<p>When <code>TRUE</code>, indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When <code>FALSE</code>, indicates that the configured audience model resource owner will manage permissions related to the given collaboration.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model association.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the configured audience model association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured audience model association was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelAssociation) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["name"] = value["name"]
    out["manageResourcePolicies"] = value["manage_resource_policies"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ConfiguredAudienceModelAssociation:
    out: ConfiguredAudienceModelAssociation = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ConfiguredAudienceModelAssociation.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ConfiguredAudienceModelAssociation.arn required")
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociation.configured_audience_model_arn required"
        )
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociation.membership_id required"
        )
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociation.membership_arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociation.collaboration_id required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociation.collaboration_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredAudienceModelAssociation.name required")
    if "manageResourcePolicies" in data:
        out["manage_resource_policies"] = data["manageResourcePolicies"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociation.manage_resource_policies required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "createTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociation.create_time required"
        )
    if "updateTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociation.update_time required"
        )
    return out
