"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationTrainedModelInferenceJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.inference_output_configuration
    import capo_cleanroomsml.types.logs_status
    import capo_cleanroomsml.types.metrics_status
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_inference_job_arn
    import capo_cleanroomsml.types.trained_model_inference_job_status
    import capo_cleanroomsml.types.uuid


class CollaborationTrainedModelInferenceJobSummary(TypedDict, closed=True):
    trained_model_inference_job_arn: "capo_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>The Amazon Resource Name (ARN) of the trained model inference job.</p>"""
    configured_model_algorithm_association_arn: NotRequired[
        "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that is used for the trained model inference job.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the trained model inference job.</p>"""
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that is used for the trained model inference job.</p>"""
    trained_model_version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model that was used for inference in this job.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained model inference job.</p>"""
    status: "capo_cleanroomsml.types.trained_model_inference_job_status.TrainedModelInferenceJobStatus"
    """<p>The status of the trained model inference job.</p>"""
    output_configuration: "capo_cleanroomsml.types.inference_output_configuration.InferenceOutputConfiguration"
    """<p>Returns output configuration information for the trained model inference job.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model inference job.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model inference job.</p>"""
    metrics_status: NotRequired["capo_cleanroomsml.types.metrics_status.MetricsStatus"]
    """<p>the trained model inference job metrics status.</p>"""
    metrics_status_details: NotRequired["str"]
    """<p>Details about the metrics status for trained model inference job.</p>"""
    logs_status: NotRequired["capo_cleanroomsml.types.logs_status.LogsStatus"]
    """<p>The trained model inference job logs status.</p>"""
    logs_status_details: NotRequired["str"]
    """<p>Details about the logs status for the trained model inference job.</p>"""
    ml_model_inference_payer_account_id: NotRequired[
        "capo_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model inference costs.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the trained model inference job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model inference job was updated.</p>"""
    creator_account_id: "capo_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID that created the trained model inference job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationTrainedModelInferenceJobSummary) -> dict:
    out: dict = {}
    out["trainedModelInferenceJobArn"] = value["trained_model_inference_job_arn"]
    if "configured_model_algorithm_association_arn" in value:
        out["configuredModelAlgorithmAssociationArn"] = value[
            "configured_model_algorithm_association_arn"
        ]
    out["membershipIdentifier"] = value["membership_identifier"]
    out["trainedModelArn"] = value["trained_model_arn"]
    if "trained_model_version_identifier" in value:
        out["trainedModelVersionIdentifier"] = value["trained_model_version_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    import capo_cleanroomsml.types.trained_model_inference_job_status

    out["status"] = (
        capo_cleanroomsml.types.trained_model_inference_job_status.serialize_json(
            value["status"]
        )
    )
    import capo_cleanroomsml.types.inference_output_configuration

    out["outputConfiguration"] = (
        capo_cleanroomsml.types.inference_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "metrics_status" in value:
        import capo_cleanroomsml.types.metrics_status

        out["metricsStatus"] = capo_cleanroomsml.types.metrics_status.serialize_json(
            value["metrics_status"]
        )
    if "metrics_status_details" in value:
        out["metricsStatusDetails"] = value["metrics_status_details"]
    if "logs_status" in value:
        import capo_cleanroomsml.types.logs_status

        out["logsStatus"] = capo_cleanroomsml.types.logs_status.serialize_json(
            value["logs_status"]
        )
    if "logs_status_details" in value:
        out["logsStatusDetails"] = value["logs_status_details"]
    if "ml_model_inference_payer_account_id" in value:
        out["mlModelInferencePayerAccountId"] = value[
            "ml_model_inference_payer_account_id"
        ]
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["creatorAccountId"] = value["creator_account_id"]
    return out


def deserialize_json(data: dict) -> CollaborationTrainedModelInferenceJobSummary:
    out: CollaborationTrainedModelInferenceJobSummary = {}  # type: ignore[typeddict-item]
    if "trainedModelInferenceJobArn" in data:
        out["trained_model_inference_job_arn"] = data["trainedModelInferenceJobArn"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.trained_model_inference_job_arn required"
        )
    if "configuredModelAlgorithmAssociationArn" in data:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.membership_identifier required"
        )
    if "trainedModelArn" in data:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.trained_model_arn required"
        )
    if "trainedModelVersionIdentifier" in data:
        out["trained_model_version_identifier"] = data["trainedModelVersionIdentifier"]
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.collaboration_identifier required"
        )
    if "status" in data:
        import capo_cleanroomsml.types.trained_model_inference_job_status

        out["status"] = (
            capo_cleanroomsml.types.trained_model_inference_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.status required"
        )
    if "outputConfiguration" in data:
        import capo_cleanroomsml.types.inference_output_configuration

        out["output_configuration"] = (
            capo_cleanroomsml.types.inference_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.output_configuration required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "metricsStatus" in data:
        import capo_cleanroomsml.types.metrics_status

        out["metrics_status"] = capo_cleanroomsml.types.metrics_status.deserialize_json(
            data["metricsStatus"]
        )
    if "metricsStatusDetails" in data:
        out["metrics_status_details"] = data["metricsStatusDetails"]
    if "logsStatus" in data:
        import capo_cleanroomsml.types.logs_status

        out["logs_status"] = capo_cleanroomsml.types.logs_status.deserialize_json(
            data["logsStatus"]
        )
    if "logsStatusDetails" in data:
        out["logs_status_details"] = data["logsStatusDetails"]
    if "mlModelInferencePayerAccountId" in data:
        out["ml_model_inference_payer_account_id"] = data[
            "mlModelInferencePayerAccountId"
        ]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.create_time required"
        )
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.update_time required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelInferenceJobSummary.creator_account_id required"
        )
    return out
