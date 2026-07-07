"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationConfiguredAudienceModelAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_association_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_association_identifier
    import aws_sdk_cleanrooms.types.configured_audience_model_association_name
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class CollaborationConfiguredAudienceModelAssociation(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier"
    """<p>The identifier of the configured audience model association.</p>"""
    arn: "aws_sdk_cleanrooms.types.configured_audience_model_association_arn.ConfiguredAudienceModelAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model association.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier for the collaboration that the configured audience model associations belong to. Accepts collaboration ID.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the configured audience model's associated collaboration.</p>"""
    configured_audience_model_arn: "aws_sdk_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configure audience model.</p>"""
    name: "aws_sdk_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
    """<p>The name of the configured audience model association.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model association.</p>"""
    creator_account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Only supports Amazon Web Services account ID.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the configured audience model association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured audience model association was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationConfiguredAudienceModelAssociation) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["creatorAccountId"] = value["creator_account_id"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> CollaborationConfiguredAudienceModelAssociation:
    out: CollaborationConfiguredAudienceModelAssociation = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociation.id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociation.arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociation.collaboration_id required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociation.collaboration_arn required"
        )
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociation.configured_audience_model_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociation.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociation.creator_account_id required"
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
            "CollaborationConfiguredAudienceModelAssociation.create_time required"
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
            "CollaborationConfiguredAudienceModelAssociation.update_time required"
        )
    return out
