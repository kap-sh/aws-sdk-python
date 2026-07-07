"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetCollaborationMLInputChannelResponse``."""

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
    import aws_sdk_cleanroomsml.types.privacy_budgets
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.status_details
    import aws_sdk_cleanroomsml.types.synthetic_data_configuration
    import aws_sdk_cleanroomsml.types.uuid


class GetCollaborationMLInputChannelResponse(TypedDict, closed=True):
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the ML input channel.</p>"""
    collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the ML input channel.</p>"""
    ml_input_channel_arn: (
        "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the ML input channel.</p>"""
    configured_model_algorithm_associations: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList"
    """<p>The configured model algorithm associations that were used to create the ML input channel.</p>"""
    status: "aws_sdk_cleanroomsml.types.ml_input_channel_status.MLInputChannelStatus"
    """<p>The status of the ML input channel.</p>"""
    status_details: NotRequired[
        "aws_sdk_cleanroomsml.types.status_details.StatusDetails"
    ]
    retention_in_days: "int"
    """<p>The number of days to retain the data for the ML input channel.</p>"""
    number_of_records: NotRequired["int"]
    """<p>The number of records in the ML input channel.</p>"""
    privacy_budgets: NotRequired[
        "aws_sdk_cleanroomsml.types.privacy_budgets.PrivacyBudgets"
    ]
    """<p>Returns the privacy budgets that control access to this Clean Rooms ML input channel. Use these budgets to monitor and limit resource consumption over specified time periods.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ML input channel.</p>"""
    synthetic_data_configuration: NotRequired[
        "aws_sdk_cleanroomsml.types.synthetic_data_configuration.SyntheticDataConfiguration"
    ]
    """<p>The synthetic data configuration for this ML input channel, including parameters for generating privacy-preserving synthetic data and evaluation scores for measuring the privacy of the generated data.</p>"""
    payer_configuration: NotRequired[
        "aws_sdk_cleanroomsml.types.payer_configuration.PayerConfiguration"
    ]
    """<p>The payer configuration for the ML input channel.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the ML input channel was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ML input channel was updated.</p>"""
    creator_account_id: "aws_sdk_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID of the member who created the ML input channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationMLInputChannelResponse) -> dict:
    out: dict = {}
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    out["name"] = value["name"]
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list

    out["configuredModelAlgorithmAssociations"] = (
        aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.serialize_json(
            value["configured_model_algorithm_associations"]
        )
    )
    import aws_sdk_cleanroomsml.types.ml_input_channel_status

    out["status"] = aws_sdk_cleanroomsml.types.ml_input_channel_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import aws_sdk_cleanroomsml.types.status_details

        out["statusDetails"] = aws_sdk_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    out["retentionInDays"] = value["retention_in_days"]
    if "number_of_records" in value:
        out["numberOfRecords"] = value["number_of_records"]
    if "privacy_budgets" in value:
        import aws_sdk_cleanroomsml.types.privacy_budgets

        out["privacyBudgets"] = (
            aws_sdk_cleanroomsml.types.privacy_budgets.serialize_json(
                value["privacy_budgets"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "synthetic_data_configuration" in value:
        import aws_sdk_cleanroomsml.types.synthetic_data_configuration

        out["syntheticDataConfiguration"] = (
            aws_sdk_cleanroomsml.types.synthetic_data_configuration.serialize_json(
                value["synthetic_data_configuration"]
            )
        )
    if "payer_configuration" in value:
        import aws_sdk_cleanroomsml.types.payer_configuration

        out["payerConfiguration"] = (
            aws_sdk_cleanroomsml.types.payer_configuration.serialize_json(
                value["payer_configuration"]
            )
        )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["creatorAccountId"] = value["creator_account_id"]
    return out


def deserialize_json(data: dict) -> GetCollaborationMLInputChannelResponse:
    out: GetCollaborationMLInputChannelResponse = {}  # type: ignore[typeddict-item]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.membership_identifier required"
        )
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.collaboration_identifier required"
        )
    if "mlInputChannelArn" in data:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.ml_input_channel_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.name required"
        )
    if "configuredModelAlgorithmAssociations" in data:
        import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list

        out["configured_model_algorithm_associations"] = (
            aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.deserialize_json(
                data["configuredModelAlgorithmAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.configured_model_algorithm_associations required"
        )
    if "status" in data:
        import aws_sdk_cleanroomsml.types.ml_input_channel_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.ml_input_channel_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.status required"
        )
    if "statusDetails" in data:
        import aws_sdk_cleanroomsml.types.status_details

        out["status_details"] = (
            aws_sdk_cleanroomsml.types.status_details.deserialize_json(
                data["statusDetails"]
            )
        )
    if "retentionInDays" in data:
        out["retention_in_days"] = data["retentionInDays"]
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.retention_in_days required"
        )
    if "numberOfRecords" in data:
        out["number_of_records"] = data["numberOfRecords"]
    if "privacyBudgets" in data:
        import aws_sdk_cleanroomsml.types.privacy_budgets

        out["privacy_budgets"] = (
            aws_sdk_cleanroomsml.types.privacy_budgets.deserialize_json(
                data["privacyBudgets"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "syntheticDataConfiguration" in data:
        import aws_sdk_cleanroomsml.types.synthetic_data_configuration

        out["synthetic_data_configuration"] = (
            aws_sdk_cleanroomsml.types.synthetic_data_configuration.deserialize_json(
                data["syntheticDataConfiguration"]
            )
        )
    if "payerConfiguration" in data:
        import aws_sdk_cleanroomsml.types.payer_configuration

        out["payer_configuration"] = (
            aws_sdk_cleanroomsml.types.payer_configuration.deserialize_json(
                data["payerConfiguration"]
            )
        )
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.create_time required"
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
            "GetCollaborationMLInputChannelResponse.update_time required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "GetCollaborationMLInputChannelResponse.creator_account_id required"
        )
    return out
