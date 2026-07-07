"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationConfiguredAudienceModelAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_association_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_association_identifier
    import aws_sdk_cleanrooms.types.configured_audience_model_association_name
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class CollaborationConfiguredAudienceModelAssociationSummary(TypedDict, closed=True):
    arn: "aws_sdk_cleanrooms.types.configured_audience_model_association_arn.ConfiguredAudienceModelAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model association.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the configured audience model association was created.</p>"""
    id: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier"
    """<p>The identifier of the configured audience model association.</p>"""
    name: "aws_sdk_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
    """<p>The name of the configured audience model association.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured audience model association was updated.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the configured audience model's associated collaboration.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier for the collaboration that the configured audience model associations belong to. Accepts collaboration ID.</p>"""
    creator_account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Only supports Amazon Web Services account ID.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: CollaborationConfiguredAudienceModelAssociationSummary,
) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["creatorAccountId"] = value["creator_account_id"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(
    data: dict,
) -> CollaborationConfiguredAudienceModelAssociationSummary:
    out: CollaborationConfiguredAudienceModelAssociationSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociationSummary.arn required"
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
            "CollaborationConfiguredAudienceModelAssociationSummary.create_time required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociationSummary.id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociationSummary.name required"
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
            "CollaborationConfiguredAudienceModelAssociationSummary.update_time required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociationSummary.collaboration_arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociationSummary.collaboration_id required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredAudienceModelAssociationSummary.creator_account_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
