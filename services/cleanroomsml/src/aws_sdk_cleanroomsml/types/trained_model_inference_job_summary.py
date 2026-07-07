"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.account_id
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn
    import aws_sdk_cleanroomsml.types.inference_output_configuration
    import aws_sdk_cleanroomsml.types.logs_status
    import aws_sdk_cleanroomsml.types.metrics_status
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_arn
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_status
    import aws_sdk_cleanroomsml.types.uuid


class TrainedModelInferenceJobSummary(TypedDict, closed=True):
    trained_model_inference_job_arn: "aws_sdk_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>The Amazon Resource Name (ARN) of the trained model inference job.</p>"""
    configured_model_algorithm_association_arn: NotRequired[
        "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that is used for the trained model inference job.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the trained model inference job.</p>"""
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that is used for the trained model inference job.</p>"""
    trained_model_version_identifier: NotRequired[
        "aws_sdk_cleanroomsml.types.uuid.UUID"
    ]
    """<p>The version identifier of the trained model that was used for inference in this job.</p>"""
    collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained model inference job.</p>"""
    status: "aws_sdk_cleanroomsml.types.trained_model_inference_job_status.TrainedModelInferenceJobStatus"
    """<p>The status of the trained model inference job.</p>"""
    output_configuration: "aws_sdk_cleanroomsml.types.inference_output_configuration.InferenceOutputConfiguration"
    """<p>The output configuration information of the trained model job.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model inference job.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model inference job.</p>"""
    metrics_status: NotRequired[
        "aws_sdk_cleanroomsml.types.metrics_status.MetricsStatus"
    ]
    """<p>The metric status of the trained model inference job.</p>"""
    metrics_status_details: NotRequired["str"]
    """<p>Details about the metrics status for the trained model inference job.</p>"""
    logs_status: NotRequired["aws_sdk_cleanroomsml.types.logs_status.LogsStatus"]
    """<p>The log status of the trained model inference job.</p>"""
    logs_status_details: NotRequired["str"]
    """<p>Details about the log status for the trained model inference job.</p>"""
    ml_model_inference_payer_account_id: NotRequired[
        "aws_sdk_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model inference costs.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the trained model inference job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model inference job was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelInferenceJobSummary) -> dict:
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
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_status

    out["status"] = (
        aws_sdk_cleanroomsml.types.trained_model_inference_job_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_cleanroomsml.types.inference_output_configuration

    out["outputConfiguration"] = (
        aws_sdk_cleanroomsml.types.inference_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
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
    if "ml_model_inference_payer_account_id" in value:
        out["mlModelInferencePayerAccountId"] = value[
            "ml_model_inference_payer_account_id"
        ]
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> TrainedModelInferenceJobSummary:
    out: TrainedModelInferenceJobSummary = {}  # type: ignore[typeddict-item]
    if "trainedModelInferenceJobArn" in data:
        out["trained_model_inference_job_arn"] = data["trainedModelInferenceJobArn"]
    else:
        raise DeserializationError(
            "TrainedModelInferenceJobSummary.trained_model_inference_job_arn required"
        )
    if "configuredModelAlgorithmAssociationArn" in data:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "TrainedModelInferenceJobSummary.membership_identifier required"
        )
    if "trainedModelArn" in data:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        raise DeserializationError(
            "TrainedModelInferenceJobSummary.trained_model_arn required"
        )
    if "trainedModelVersionIdentifier" in data:
        out["trained_model_version_identifier"] = data["trainedModelVersionIdentifier"]
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "TrainedModelInferenceJobSummary.collaboration_identifier required"
        )
    if "status" in data:
        import aws_sdk_cleanroomsml.types.trained_model_inference_job_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.trained_model_inference_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("TrainedModelInferenceJobSummary.status required")
    if "outputConfiguration" in data:
        import aws_sdk_cleanroomsml.types.inference_output_configuration

        out["output_configuration"] = (
            aws_sdk_cleanroomsml.types.inference_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "TrainedModelInferenceJobSummary.output_configuration required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TrainedModelInferenceJobSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
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
    if "mlModelInferencePayerAccountId" in data:
        out["ml_model_inference_payer_account_id"] = data[
            "mlModelInferencePayerAccountId"
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
            "TrainedModelInferenceJobSummary.create_time required"
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
            "TrainedModelInferenceJobSummary.update_time required"
        )
    return out
