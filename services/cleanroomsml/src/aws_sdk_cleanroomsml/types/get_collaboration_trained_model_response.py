"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetCollaborationTrainedModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.account_id
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn
    import aws_sdk_cleanroomsml.types.incremental_training_data_channels_output
    import aws_sdk_cleanroomsml.types.logs_status
    import aws_sdk_cleanroomsml.types.metrics_status
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_config
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.status_details
    import aws_sdk_cleanroomsml.types.stopping_condition
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.trained_model_status
    import aws_sdk_cleanroomsml.types.training_input_mode
    import aws_sdk_cleanroomsml.types.uuid


class GetCollaborationTrainedModelResponse(TypedDict, closed=True):
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that created the trained model.</p>"""
    collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained model.</p>"""
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model.</p>"""
    version_identifier: NotRequired["aws_sdk_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model. This unique identifier distinguishes this version from other versions of the same trained model.</p>"""
    incremental_training_data_channels: NotRequired[
        "aws_sdk_cleanroomsml.types.incremental_training_data_channels_output.IncrementalTrainingDataChannelsOutput"
    ]
    """<p>Information about the incremental training data channels used to create this version of the trained model. This includes details about the base model that was used for incremental training and the channel configuration.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model.</p>"""
    status: "aws_sdk_cleanroomsml.types.trained_model_status.TrainedModelStatus"
    """<p>The status of the trained model.</p>"""
    status_details: NotRequired[
        "aws_sdk_cleanroomsml.types.status_details.StatusDetails"
    ]
    configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that was used to create this trained model.</p>"""
    resource_config: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_config.ResourceConfig"
    ]
    """<p>The EC2 resource configuration that was used to train this model.</p>"""
    training_input_mode: NotRequired[
        "aws_sdk_cleanroomsml.types.training_input_mode.TrainingInputMode"
    ]
    """<p>The input mode that was used for accessing the training data when this trained model was created. This indicates how the training data was made available to the training algorithm.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_cleanroomsml.types.stopping_condition.StoppingCondition"
    ]
    """<p>The stopping condition that determined when model training ended.</p>"""
    metrics_status: NotRequired[
        "aws_sdk_cleanroomsml.types.metrics_status.MetricsStatus"
    ]
    """<p>The status of the model metrics.</p>"""
    metrics_status_details: NotRequired["str"]
    """<p>Details about the status information for the model metrics.</p>"""
    logs_status: NotRequired["aws_sdk_cleanroomsml.types.logs_status.LogsStatus"]
    """<p>Status information for the logs.</p>"""
    logs_status_details: NotRequired["str"]
    """<p>Details about the status information for the logs.</p>"""
    training_container_image_digest: NotRequired["str"]
    """<p>Information about the training container image.</p>"""
    ml_model_training_payer_account_id: NotRequired[
        "aws_sdk_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model training costs.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the trained model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model was updated.</p>"""
    creator_account_id: "aws_sdk_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID of the member that created the trained model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationTrainedModelResponse) -> dict:
    out: dict = {}
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["trainedModelArn"] = value["trained_model_arn"]
    if "version_identifier" in value:
        out["versionIdentifier"] = value["version_identifier"]
    if "incremental_training_data_channels" in value:
        import aws_sdk_cleanroomsml.types.incremental_training_data_channels_output

        out["incrementalTrainingDataChannels"] = (
            aws_sdk_cleanroomsml.types.incremental_training_data_channels_output.serialize_json(
                value["incremental_training_data_channels"]
            )
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_cleanroomsml.types.trained_model_status

    out["status"] = aws_sdk_cleanroomsml.types.trained_model_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import aws_sdk_cleanroomsml.types.status_details

        out["statusDetails"] = aws_sdk_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    out["configuredModelAlgorithmAssociationArn"] = value[
        "configured_model_algorithm_association_arn"
    ]
    if "resource_config" in value:
        import aws_sdk_cleanroomsml.types.resource_config

        out["resourceConfig"] = (
            aws_sdk_cleanroomsml.types.resource_config.serialize_json(
                value["resource_config"]
            )
        )
    if "training_input_mode" in value:
        import aws_sdk_cleanroomsml.types.training_input_mode

        out["trainingInputMode"] = (
            aws_sdk_cleanroomsml.types.training_input_mode.serialize_json(
                value["training_input_mode"]
            )
        )
    if "stopping_condition" in value:
        import aws_sdk_cleanroomsml.types.stopping_condition

        out["stoppingCondition"] = (
            aws_sdk_cleanroomsml.types.stopping_condition.serialize_json(
                value["stopping_condition"]
            )
        )
    if "metrics_status" in value:
        import aws_sdk_cleanroomsml.types.metrics_status

        out["metricsStatus"] = aws_sdk_cleanroomsml.types.metrics_status.serialize_json(
            value["metrics_status"]
        )
    if "metrics_status_details" in value:
        out["metricsStatusDetails"] = value["metrics_status_details"]
    if "logs_status" in value:
        import aws_sdk_cleanroomsml.types.logs_status

        out["logsStatus"] = aws_sdk_cleanroomsml.types.logs_status.serialize_json(
            value["logs_status"]
        )
    if "logs_status_details" in value:
        out["logsStatusDetails"] = value["logs_status_details"]
    if "training_container_image_digest" in value:
        out["trainingContainerImageDigest"] = value["training_container_image_digest"]
    if "ml_model_training_payer_account_id" in value:
        out["mlModelTrainingPayerAccountId"] = value[
            "ml_model_training_payer_account_id"
        ]
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


def deserialize_json(data: dict) -> GetCollaborationTrainedModelResponse:
    out: GetCollaborationTrainedModelResponse = {}  # type: ignore[typeddict-item]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "GetCollaborationTrainedModelResponse.membership_identifier required"
        )
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "GetCollaborationTrainedModelResponse.collaboration_identifier required"
        )
    if "trainedModelArn" in data:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        raise DeserializationError(
            "GetCollaborationTrainedModelResponse.trained_model_arn required"
        )
    if "versionIdentifier" in data:
        out["version_identifier"] = data["versionIdentifier"]
    if "incrementalTrainingDataChannels" in data:
        import aws_sdk_cleanroomsml.types.incremental_training_data_channels_output

        out["incremental_training_data_channels"] = (
            aws_sdk_cleanroomsml.types.incremental_training_data_channels_output.deserialize_json(
                data["incrementalTrainingDataChannels"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetCollaborationTrainedModelResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_cleanroomsml.types.trained_model_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.trained_model_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationTrainedModelResponse.status required"
        )
    if "statusDetails" in data:
        import aws_sdk_cleanroomsml.types.status_details

        out["status_details"] = (
            aws_sdk_cleanroomsml.types.status_details.deserialize_json(
                data["statusDetails"]
            )
        )
    if "configuredModelAlgorithmAssociationArn" in data:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    else:
        raise DeserializationError(
            "GetCollaborationTrainedModelResponse.configured_model_algorithm_association_arn required"
        )
    if "resourceConfig" in data:
        import aws_sdk_cleanroomsml.types.resource_config

        out["resource_config"] = (
            aws_sdk_cleanroomsml.types.resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    if "trainingInputMode" in data:
        import aws_sdk_cleanroomsml.types.training_input_mode

        out["training_input_mode"] = (
            aws_sdk_cleanroomsml.types.training_input_mode.deserialize_json(
                data["trainingInputMode"]
            )
        )
    if "stoppingCondition" in data:
        import aws_sdk_cleanroomsml.types.stopping_condition

        out["stopping_condition"] = (
            aws_sdk_cleanroomsml.types.stopping_condition.deserialize_json(
                data["stoppingCondition"]
            )
        )
    if "metricsStatus" in data:
        import aws_sdk_cleanroomsml.types.metrics_status

        out["metrics_status"] = (
            aws_sdk_cleanroomsml.types.metrics_status.deserialize_json(
                data["metricsStatus"]
            )
        )
    if "metricsStatusDetails" in data:
        out["metrics_status_details"] = data["metricsStatusDetails"]
    if "logsStatus" in data:
        import aws_sdk_cleanroomsml.types.logs_status

        out["logs_status"] = aws_sdk_cleanroomsml.types.logs_status.deserialize_json(
            data["logsStatus"]
        )
    if "logsStatusDetails" in data:
        out["logs_status_details"] = data["logsStatusDetails"]
    if "trainingContainerImageDigest" in data:
        out["training_container_image_digest"] = data["trainingContainerImageDigest"]
    if "mlModelTrainingPayerAccountId" in data:
        out["ml_model_training_payer_account_id"] = data[
            "mlModelTrainingPayerAccountId"
        ]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationTrainedModelResponse.create_time required"
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
            "GetCollaborationTrainedModelResponse.update_time required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "GetCollaborationTrainedModelResponse.creator_account_id required"
        )
    return out
