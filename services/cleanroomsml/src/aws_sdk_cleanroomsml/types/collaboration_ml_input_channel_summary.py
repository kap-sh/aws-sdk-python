"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationMLInputChannelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.account_id
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import aws_sdk_cleanroomsml.types.ml_input_channel_arn
    import aws_sdk_cleanroomsml.types.ml_input_channel_status
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.payer_configuration
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.uuid


class CollaborationMLInputChannelSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the ML input channel was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ML input channel was updated.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the ML input channel.</p>"""
    collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the ML input channel.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the ML input channel.</p>"""
    configured_model_algorithm_associations: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList"
    """<p>The associated configured model algorithms used to create the ML input channel.</p>"""
    ml_input_channel_arn: (
        "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel.</p>"""
    status: "aws_sdk_cleanroomsml.types.ml_input_channel_status.MLInputChannelStatus"
    """<p>The status of the ML input channel.</p>"""
    creator_account_id: "aws_sdk_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID of the member who created the ML input channel.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ML input channel.</p>"""
    payer_configuration: NotRequired[
        "aws_sdk_cleanroomsml.types.payer_configuration.PayerConfiguration"
    ]
    """<p>The payer configuration for the ML input channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationMLInputChannelSummary) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["name"] = value["name"]
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list

    out["configuredModelAlgorithmAssociations"] = (
        aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.serialize_json(
            value["configured_model_algorithm_associations"]
        )
    )
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    import aws_sdk_cleanroomsml.types.ml_input_channel_status

    out["status"] = aws_sdk_cleanroomsml.types.ml_input_channel_status.serialize_json(
        value["status"]
    )
    out["creatorAccountId"] = value["creator_account_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "payer_configuration" in value:
        import aws_sdk_cleanroomsml.types.payer_configuration

        out["payerConfiguration"] = (
            aws_sdk_cleanroomsml.types.payer_configuration.serialize_json(
                value["payer_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CollaborationMLInputChannelSummary:
    out: CollaborationMLInputChannelSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.create_time required"
        )
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.update_time required"
        )
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.membership_identifier required"
        )
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.collaboration_identifier required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CollaborationMLInputChannelSummary.name required")
    if "configuredModelAlgorithmAssociations" in data:
        import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list

        out["configured_model_algorithm_associations"] = (
            aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.deserialize_json(
                data["configuredModelAlgorithmAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.configured_model_algorithm_associations required"
        )
    if "mlInputChannelArn" in data:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.ml_input_channel_arn required"
        )
    if "status" in data:
        import aws_sdk_cleanroomsml.types.ml_input_channel_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.ml_input_channel_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CollaborationMLInputChannelSummary.status required")
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.creator_account_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "payerConfiguration" in data:
        import aws_sdk_cleanroomsml.types.payer_configuration

        out["payer_configuration"] = (
            aws_sdk_cleanroomsml.types.payer_configuration.deserialize_json(
                data["payerConfiguration"]
            )
        )
    return out
