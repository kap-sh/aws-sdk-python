"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredAudienceModelAssociationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_association_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_association_name
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class ConfiguredAudienceModelAssociationSummary(TypedDict):
    membership_id: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>A unique identifier of the membership that contains the configured audience model association.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership that contains the configured audience model association.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains the configured audience model association.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier of the collaboration that configured audience model is associated with.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the configured audience model association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured audience model association was updated.</p>"""
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier of the configured audience model association.</p>"""
    arn: "aws_sdk_cleanrooms.types.configured_audience_model_association_arn.ConfiguredAudienceModelAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model association.</p>"""
    name: "aws_sdk_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
    """<p>The name of the configured audience model association.</p>"""
    configured_audience_model_arn: "aws_sdk_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that was used for this configured audience model association.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelAssociationSummary) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ConfiguredAudienceModelAssociationSummary:
    out: ConfiguredAudienceModelAssociationSummary = {}  # type: ignore[typeddict-item]
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.membership_id required"
        )
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.membership_arn required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.collaboration_arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.collaboration_id required"
        )
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.create_time required"
        )
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.update_time required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.name required"
        )
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.configured_audience_model_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
