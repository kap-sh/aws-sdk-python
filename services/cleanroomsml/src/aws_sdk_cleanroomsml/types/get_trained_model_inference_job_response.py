"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetTrainedModelInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.account_id
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn
    import aws_sdk_cleanroomsml.types.inference_container_execution_parameters
    import aws_sdk_cleanroomsml.types.inference_environment_map
    import aws_sdk_cleanroomsml.types.inference_output_configuration
    import aws_sdk_cleanroomsml.types.inference_resource_config
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.logs_status
    import aws_sdk_cleanroomsml.types.metrics_status
    import aws_sdk_cleanroomsml.types.model_inference_data_source
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.status_details
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_arn
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_status
    import aws_sdk_cleanroomsml.types.uuid


class GetTrainedModelInferenceJobResponse(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the trained model inference job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model inference job was updated.</p>"""
    trained_model_inference_job_arn: "aws_sdk_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>The Amazon Resource Name (ARN) of the trained model inference job.</p>"""
    configured_model_algorithm_association_arn: NotRequired[
        "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that was used for the trained model inference job.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model inference job.</p>"""
    status: "aws_sdk_cleanroomsml.types.trained_model_inference_job_status.TrainedModelInferenceJobStatus"
    """<p>The status of the trained model inference job.</p>"""
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) for the trained model that was used for the trained model inference job.</p>"""
    trained_model_version_identifier: NotRequired[
        "aws_sdk_cleanroomsml.types.uuid.UUID"
    ]
    """<p>The version identifier of the trained model used for this inference job. This identifies the specific version of the trained model that was used to generate the inference results.</p>"""
    resource_config: (
        "aws_sdk_cleanroomsml.types.inference_resource_config.InferenceResourceConfig"
    )
    """<p>The resource configuration information for the trained model inference job.</p>"""
    output_configuration: "aws_sdk_cleanroomsml.types.inference_output_configuration.InferenceOutputConfiguration"
    """<p>The output configuration information for the trained model inference job.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the trained model inference job.</p>"""
    data_source: "aws_sdk_cleanroomsml.types.model_inference_data_source.ModelInferenceDataSource"
    """<p>The data source that was used for the trained model inference job.</p>"""
    container_execution_parameters: NotRequired[
        "aws_sdk_cleanroomsml.types.inference_container_execution_parameters.InferenceContainerExecutionParameters"
    ]
    """<p>The execution parameters for the model inference job container.</p>"""
    status_details: NotRequired[
        "aws_sdk_cleanroomsml.types.status_details.StatusDetails"
    ]
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model inference job.</p>"""
    inference_container_image_digest: NotRequired["str"]
    """<p>Information about the training container image.</p>"""
    environment: NotRequired[
        "aws_sdk_cleanroomsml.types.inference_environment_map.InferenceEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container.</p>"""
    kms_key_arn: NotRequired["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the ML inference job and associated data.</p>"""
    metrics_status: NotRequired[
        "aws_sdk_cleanroomsml.types.metrics_status.MetricsStatus"
    ]
    """<p>The metrics status for the trained model inference job.</p>"""
    metrics_status_details: NotRequired["str"]
    """<p>Details about the metrics status for the trained model inference job.</p>"""
    logs_status: NotRequired["aws_sdk_cleanroomsml.types.logs_status.LogsStatus"]
    """<p>The logs status for the trained model inference job.</p>"""
    logs_status_details: NotRequired["str"]
    """<p>Details about the logs status for the trained model inference job.</p>"""
    tags: NotRequired["aws_sdk_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you applied to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    ml_model_inference_payer_account_id: NotRequired[
        "aws_sdk_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model inference costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainedModelInferenceJobResponse) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["trainedModelInferenceJobArn"] = value["trained_model_inference_job_arn"]
    if "configured_model_algorithm_association_arn" in value:
        out["configuredModelAlgorithmAssociationArn"] = value[
            "configured_model_algorithm_association_arn"
        ]
    out["name"] = value["name"]
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_status

    out["status"] = (
        aws_sdk_cleanroomsml.types.trained_model_inference_job_status.serialize_json(
            value["status"]
        )
    )
    out["trainedModelArn"] = value["trained_model_arn"]
    if "trained_model_version_identifier" in value:
        out["trainedModelVersionIdentifier"] = value["trained_model_version_identifier"]
    import aws_sdk_cleanroomsml.types.inference_resource_config

    out["resourceConfig"] = (
        aws_sdk_cleanroomsml.types.inference_resource_config.serialize_json(
            value["resource_config"]
        )
    )
    import aws_sdk_cleanroomsml.types.inference_output_configuration

    out["outputConfiguration"] = (
        aws_sdk_cleanroomsml.types.inference_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    out["membershipIdentifier"] = value["membership_identifier"]
    import aws_sdk_cleanroomsml.types.model_inference_data_source

    out["dataSource"] = (
        aws_sdk_cleanroomsml.types.model_inference_data_source.serialize_json(
            value["data_source"]
        )
    )
    if "container_execution_parameters" in value:
        import aws_sdk_cleanroomsml.types.inference_container_execution_parameters

        out["containerExecutionParameters"] = (
            aws_sdk_cleanroomsml.types.inference_container_execution_parameters.serialize_json(
                value["container_execution_parameters"]
            )
        )
    if "status_details" in value:
        import aws_sdk_cleanroomsml.types.status_details

        out["statusDetails"] = aws_sdk_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "inference_container_image_digest" in value:
        out["inferenceContainerImageDigest"] = value["inference_container_image_digest"]
    if "environment" in value:
        import aws_sdk_cleanroomsml.types.inference_environment_map

        out["environment"] = (
            aws_sdk_cleanroomsml.types.inference_environment_map.serialize_json(
                value["environment"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
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
    if "tags" in value:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "ml_model_inference_payer_account_id" in value:
        out["mlModelInferencePayerAccountId"] = value[
            "ml_model_inference_payer_account_id"
        ]
    return out


def deserialize_json(data: dict) -> GetTrainedModelInferenceJobResponse:
    out: GetTrainedModelInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.create_time required"
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
            "GetTrainedModelInferenceJobResponse.update_time required"
        )
    if "trainedModelInferenceJobArn" in data:
        out["trained_model_inference_job_arn"] = data["trainedModelInferenceJobArn"]
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.trained_model_inference_job_arn required"
        )
    if "configuredModelAlgorithmAssociationArn" in data:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetTrainedModelInferenceJobResponse.name required")
    if "status" in data:
        import aws_sdk_cleanroomsml.types.trained_model_inference_job_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.trained_model_inference_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.status required"
        )
    if "trainedModelArn" in data:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.trained_model_arn required"
        )
    if "trainedModelVersionIdentifier" in data:
        out["trained_model_version_identifier"] = data["trainedModelVersionIdentifier"]
    if "resourceConfig" in data:
        import aws_sdk_cleanroomsml.types.inference_resource_config

        out["resource_config"] = (
            aws_sdk_cleanroomsml.types.inference_resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.resource_config required"
        )
    if "outputConfiguration" in data:
        import aws_sdk_cleanroomsml.types.inference_output_configuration

        out["output_configuration"] = (
            aws_sdk_cleanroomsml.types.inference_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.output_configuration required"
        )
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.membership_identifier required"
        )
    if "dataSource" in data:
        import aws_sdk_cleanroomsml.types.model_inference_data_source

        out["data_source"] = (
            aws_sdk_cleanroomsml.types.model_inference_data_source.deserialize_json(
                data["dataSource"]
            )
        )
    else:
        raise DeserializationError(
            "GetTrainedModelInferenceJobResponse.data_source required"
        )
    if "containerExecutionParameters" in data:
        import aws_sdk_cleanroomsml.types.inference_container_execution_parameters

        out["container_execution_parameters"] = (
            aws_sdk_cleanroomsml.types.inference_container_execution_parameters.deserialize_json(
                data["containerExecutionParameters"]
            )
        )
    if "statusDetails" in data:
        import aws_sdk_cleanroomsml.types.status_details

        out["status_details"] = (
            aws_sdk_cleanroomsml.types.status_details.deserialize_json(
                data["statusDetails"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "inferenceContainerImageDigest" in data:
        out["inference_container_image_digest"] = data["inferenceContainerImageDigest"]
    if "environment" in data:
        import aws_sdk_cleanroomsml.types.inference_environment_map

        out["environment"] = (
            aws_sdk_cleanroomsml.types.inference_environment_map.deserialize_json(
                data["environment"]
            )
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
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
    if "tags" in data:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if "mlModelInferencePayerAccountId" in data:
        out["ml_model_inference_payer_account_id"] = data[
            "mlModelInferencePayerAccountId"
        ]
    return out
