"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExecutionStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_step_metadata
    import aws_sdk_sagemaker.types.bedrock_custom_model_deployment_metadata
    import aws_sdk_sagemaker.types.bedrock_custom_model_metadata
    import aws_sdk_sagemaker.types.bedrock_model_import_metadata
    import aws_sdk_sagemaker.types.bedrock_provisioned_model_throughput_metadata
    import aws_sdk_sagemaker.types.callback_step_metadata
    import aws_sdk_sagemaker.types.clarify_check_step_metadata
    import aws_sdk_sagemaker.types.condition_step_metadata
    import aws_sdk_sagemaker.types.emr_step_metadata
    import aws_sdk_sagemaker.types.endpoint_config_step_metadata
    import aws_sdk_sagemaker.types.endpoint_step_metadata
    import aws_sdk_sagemaker.types.fail_step_metadata
    import aws_sdk_sagemaker.types.inference_component_metadata
    import aws_sdk_sagemaker.types.job_step_metadata
    import aws_sdk_sagemaker.types.lambda_step_metadata
    import aws_sdk_sagemaker.types.lineage_metadata
    import aws_sdk_sagemaker.types.model_step_metadata
    import aws_sdk_sagemaker.types.processing_job_step_metadata
    import aws_sdk_sagemaker.types.quality_check_step_metadata
    import aws_sdk_sagemaker.types.register_model_step_metadata
    import aws_sdk_sagemaker.types.training_job_step_metadata
    import aws_sdk_sagemaker.types.transform_job_step_metadata
    import aws_sdk_sagemaker.types.tuning_job_step_meta_data

PipelineExecutionStepMetadata = TypedDict(
    "PipelineExecutionStepMetadata",
    {
        "training_job": NotRequired[
            "aws_sdk_sagemaker.types.training_job_step_metadata.TrainingJobStepMetadata"
        ],
        "processing_job": NotRequired[
            "aws_sdk_sagemaker.types.processing_job_step_metadata.ProcessingJobStepMetadata"
        ],
        "transform_job": NotRequired[
            "aws_sdk_sagemaker.types.transform_job_step_metadata.TransformJobStepMetadata"
        ],
        "tuning_job": NotRequired[
            "aws_sdk_sagemaker.types.tuning_job_step_meta_data.TuningJobStepMetaData"
        ],
        "model": NotRequired[
            "aws_sdk_sagemaker.types.model_step_metadata.ModelStepMetadata"
        ],
        "register_model": NotRequired[
            "aws_sdk_sagemaker.types.register_model_step_metadata.RegisterModelStepMetadata"
        ],
        "condition": NotRequired[
            "aws_sdk_sagemaker.types.condition_step_metadata.ConditionStepMetadata"
        ],
        "callback": NotRequired[
            "aws_sdk_sagemaker.types.callback_step_metadata.CallbackStepMetadata"
        ],
        "lambda": NotRequired[
            "aws_sdk_sagemaker.types.lambda_step_metadata.LambdaStepMetadata"
        ],
        "emr": NotRequired["aws_sdk_sagemaker.types.emr_step_metadata.EMRStepMetadata"],
        "quality_check": NotRequired[
            "aws_sdk_sagemaker.types.quality_check_step_metadata.QualityCheckStepMetadata"
        ],
        "clarify_check": NotRequired[
            "aws_sdk_sagemaker.types.clarify_check_step_metadata.ClarifyCheckStepMetadata"
        ],
        "fail": NotRequired[
            "aws_sdk_sagemaker.types.fail_step_metadata.FailStepMetadata"
        ],
        "auto_ml_job": NotRequired[
            "aws_sdk_sagemaker.types.auto_ml_job_step_metadata.AutoMLJobStepMetadata"
        ],
        "endpoint": NotRequired[
            "aws_sdk_sagemaker.types.endpoint_step_metadata.EndpointStepMetadata"
        ],
        "endpoint_config": NotRequired[
            "aws_sdk_sagemaker.types.endpoint_config_step_metadata.EndpointConfigStepMetadata"
        ],
        "bedrock_custom_model": NotRequired[
            "aws_sdk_sagemaker.types.bedrock_custom_model_metadata.BedrockCustomModelMetadata"
        ],
        "bedrock_custom_model_deployment": NotRequired[
            "aws_sdk_sagemaker.types.bedrock_custom_model_deployment_metadata.BedrockCustomModelDeploymentMetadata"
        ],
        "bedrock_provisioned_model_throughput": NotRequired[
            "aws_sdk_sagemaker.types.bedrock_provisioned_model_throughput_metadata.BedrockProvisionedModelThroughputMetadata"
        ],
        "bedrock_model_import": NotRequired[
            "aws_sdk_sagemaker.types.bedrock_model_import_metadata.BedrockModelImportMetadata"
        ],
        "inference_component": NotRequired[
            "aws_sdk_sagemaker.types.inference_component_metadata.InferenceComponentMetadata"
        ],
        "lineage": NotRequired[
            "aws_sdk_sagemaker.types.lineage_metadata.LineageMetadata"
        ],
        "job": NotRequired["aws_sdk_sagemaker.types.job_step_metadata.JobStepMetadata"],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionStepMetadata) -> dict:
    out: dict = {}
    if "training_job" in value:
        import aws_sdk_sagemaker.types.training_job_step_metadata

        out["TrainingJob"] = (
            aws_sdk_sagemaker.types.training_job_step_metadata.serialize_aws_json_1_1(
                value["training_job"]
            )
        )
    if "processing_job" in value:
        import aws_sdk_sagemaker.types.processing_job_step_metadata

        out["ProcessingJob"] = (
            aws_sdk_sagemaker.types.processing_job_step_metadata.serialize_aws_json_1_1(
                value["processing_job"]
            )
        )
    if "transform_job" in value:
        import aws_sdk_sagemaker.types.transform_job_step_metadata

        out["TransformJob"] = (
            aws_sdk_sagemaker.types.transform_job_step_metadata.serialize_aws_json_1_1(
                value["transform_job"]
            )
        )
    if "tuning_job" in value:
        import aws_sdk_sagemaker.types.tuning_job_step_meta_data

        out["TuningJob"] = (
            aws_sdk_sagemaker.types.tuning_job_step_meta_data.serialize_aws_json_1_1(
                value["tuning_job"]
            )
        )
    if "model" in value:
        import aws_sdk_sagemaker.types.model_step_metadata

        out["Model"] = (
            aws_sdk_sagemaker.types.model_step_metadata.serialize_aws_json_1_1(
                value["model"]
            )
        )
    if "register_model" in value:
        import aws_sdk_sagemaker.types.register_model_step_metadata

        out["RegisterModel"] = (
            aws_sdk_sagemaker.types.register_model_step_metadata.serialize_aws_json_1_1(
                value["register_model"]
            )
        )
    if "condition" in value:
        import aws_sdk_sagemaker.types.condition_step_metadata

        out["Condition"] = (
            aws_sdk_sagemaker.types.condition_step_metadata.serialize_aws_json_1_1(
                value["condition"]
            )
        )
    if "callback" in value:
        import aws_sdk_sagemaker.types.callback_step_metadata

        out["Callback"] = (
            aws_sdk_sagemaker.types.callback_step_metadata.serialize_aws_json_1_1(
                value["callback"]
            )
        )
    if "lambda" in value:
        import aws_sdk_sagemaker.types.lambda_step_metadata

        out["Lambda"] = (
            aws_sdk_sagemaker.types.lambda_step_metadata.serialize_aws_json_1_1(
                value["lambda"]
            )
        )
    if "emr" in value:
        import aws_sdk_sagemaker.types.emr_step_metadata

        out["EMR"] = aws_sdk_sagemaker.types.emr_step_metadata.serialize_aws_json_1_1(
            value["emr"]
        )
    if "quality_check" in value:
        import aws_sdk_sagemaker.types.quality_check_step_metadata

        out["QualityCheck"] = (
            aws_sdk_sagemaker.types.quality_check_step_metadata.serialize_aws_json_1_1(
                value["quality_check"]
            )
        )
    if "clarify_check" in value:
        import aws_sdk_sagemaker.types.clarify_check_step_metadata

        out["ClarifyCheck"] = (
            aws_sdk_sagemaker.types.clarify_check_step_metadata.serialize_aws_json_1_1(
                value["clarify_check"]
            )
        )
    if "fail" in value:
        import aws_sdk_sagemaker.types.fail_step_metadata

        out["Fail"] = aws_sdk_sagemaker.types.fail_step_metadata.serialize_aws_json_1_1(
            value["fail"]
        )
    if "auto_ml_job" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_step_metadata

        out["AutoMLJob"] = (
            aws_sdk_sagemaker.types.auto_ml_job_step_metadata.serialize_aws_json_1_1(
                value["auto_ml_job"]
            )
        )
    if "endpoint" in value:
        import aws_sdk_sagemaker.types.endpoint_step_metadata

        out["Endpoint"] = (
            aws_sdk_sagemaker.types.endpoint_step_metadata.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    if "endpoint_config" in value:
        import aws_sdk_sagemaker.types.endpoint_config_step_metadata

        out["EndpointConfig"] = (
            aws_sdk_sagemaker.types.endpoint_config_step_metadata.serialize_aws_json_1_1(
                value["endpoint_config"]
            )
        )
    if "bedrock_custom_model" in value:
        import aws_sdk_sagemaker.types.bedrock_custom_model_metadata

        out["BedrockCustomModel"] = (
            aws_sdk_sagemaker.types.bedrock_custom_model_metadata.serialize_aws_json_1_1(
                value["bedrock_custom_model"]
            )
        )
    if "bedrock_custom_model_deployment" in value:
        import aws_sdk_sagemaker.types.bedrock_custom_model_deployment_metadata

        out["BedrockCustomModelDeployment"] = (
            aws_sdk_sagemaker.types.bedrock_custom_model_deployment_metadata.serialize_aws_json_1_1(
                value["bedrock_custom_model_deployment"]
            )
        )
    if "bedrock_provisioned_model_throughput" in value:
        import aws_sdk_sagemaker.types.bedrock_provisioned_model_throughput_metadata

        out["BedrockProvisionedModelThroughput"] = (
            aws_sdk_sagemaker.types.bedrock_provisioned_model_throughput_metadata.serialize_aws_json_1_1(
                value["bedrock_provisioned_model_throughput"]
            )
        )
    if "bedrock_model_import" in value:
        import aws_sdk_sagemaker.types.bedrock_model_import_metadata

        out["BedrockModelImport"] = (
            aws_sdk_sagemaker.types.bedrock_model_import_metadata.serialize_aws_json_1_1(
                value["bedrock_model_import"]
            )
        )
    if "inference_component" in value:
        import aws_sdk_sagemaker.types.inference_component_metadata

        out["InferenceComponent"] = (
            aws_sdk_sagemaker.types.inference_component_metadata.serialize_aws_json_1_1(
                value["inference_component"]
            )
        )
    if "lineage" in value:
        import aws_sdk_sagemaker.types.lineage_metadata

        out["Lineage"] = (
            aws_sdk_sagemaker.types.lineage_metadata.serialize_aws_json_1_1(
                value["lineage"]
            )
        )
    if "job" in value:
        import aws_sdk_sagemaker.types.job_step_metadata

        out["Job"] = aws_sdk_sagemaker.types.job_step_metadata.serialize_aws_json_1_1(
            value["job"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionStepMetadata:
    out: PipelineExecutionStepMetadata = {}  # type: ignore[typeddict-item]
    if "TrainingJob" in data:
        import aws_sdk_sagemaker.types.training_job_step_metadata

        out["training_job"] = (
            aws_sdk_sagemaker.types.training_job_step_metadata.deserialize_aws_json_1_1(
                data["TrainingJob"]
            )
        )
    if "ProcessingJob" in data:
        import aws_sdk_sagemaker.types.processing_job_step_metadata

        out["processing_job"] = (
            aws_sdk_sagemaker.types.processing_job_step_metadata.deserialize_aws_json_1_1(
                data["ProcessingJob"]
            )
        )
    if "TransformJob" in data:
        import aws_sdk_sagemaker.types.transform_job_step_metadata

        out["transform_job"] = (
            aws_sdk_sagemaker.types.transform_job_step_metadata.deserialize_aws_json_1_1(
                data["TransformJob"]
            )
        )
    if "TuningJob" in data:
        import aws_sdk_sagemaker.types.tuning_job_step_meta_data

        out["tuning_job"] = (
            aws_sdk_sagemaker.types.tuning_job_step_meta_data.deserialize_aws_json_1_1(
                data["TuningJob"]
            )
        )
    if "Model" in data:
        import aws_sdk_sagemaker.types.model_step_metadata

        out["model"] = (
            aws_sdk_sagemaker.types.model_step_metadata.deserialize_aws_json_1_1(
                data["Model"]
            )
        )
    if "RegisterModel" in data:
        import aws_sdk_sagemaker.types.register_model_step_metadata

        out["register_model"] = (
            aws_sdk_sagemaker.types.register_model_step_metadata.deserialize_aws_json_1_1(
                data["RegisterModel"]
            )
        )
    if "Condition" in data:
        import aws_sdk_sagemaker.types.condition_step_metadata

        out["condition"] = (
            aws_sdk_sagemaker.types.condition_step_metadata.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    if "Callback" in data:
        import aws_sdk_sagemaker.types.callback_step_metadata

        out["callback"] = (
            aws_sdk_sagemaker.types.callback_step_metadata.deserialize_aws_json_1_1(
                data["Callback"]
            )
        )
    if "Lambda" in data:
        import aws_sdk_sagemaker.types.lambda_step_metadata

        out["lambda"] = (
            aws_sdk_sagemaker.types.lambda_step_metadata.deserialize_aws_json_1_1(
                data["Lambda"]
            )
        )
    if "EMR" in data:
        import aws_sdk_sagemaker.types.emr_step_metadata

        out["emr"] = aws_sdk_sagemaker.types.emr_step_metadata.deserialize_aws_json_1_1(
            data["EMR"]
        )
    if "QualityCheck" in data:
        import aws_sdk_sagemaker.types.quality_check_step_metadata

        out["quality_check"] = (
            aws_sdk_sagemaker.types.quality_check_step_metadata.deserialize_aws_json_1_1(
                data["QualityCheck"]
            )
        )
    if "ClarifyCheck" in data:
        import aws_sdk_sagemaker.types.clarify_check_step_metadata

        out["clarify_check"] = (
            aws_sdk_sagemaker.types.clarify_check_step_metadata.deserialize_aws_json_1_1(
                data["ClarifyCheck"]
            )
        )
    if "Fail" in data:
        import aws_sdk_sagemaker.types.fail_step_metadata

        out["fail"] = (
            aws_sdk_sagemaker.types.fail_step_metadata.deserialize_aws_json_1_1(
                data["Fail"]
            )
        )
    if "AutoMLJob" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_step_metadata

        out["auto_ml_job"] = (
            aws_sdk_sagemaker.types.auto_ml_job_step_metadata.deserialize_aws_json_1_1(
                data["AutoMLJob"]
            )
        )
    if "Endpoint" in data:
        import aws_sdk_sagemaker.types.endpoint_step_metadata

        out["endpoint"] = (
            aws_sdk_sagemaker.types.endpoint_step_metadata.deserialize_aws_json_1_1(
                data["Endpoint"]
            )
        )
    if "EndpointConfig" in data:
        import aws_sdk_sagemaker.types.endpoint_config_step_metadata

        out["endpoint_config"] = (
            aws_sdk_sagemaker.types.endpoint_config_step_metadata.deserialize_aws_json_1_1(
                data["EndpointConfig"]
            )
        )
    if "BedrockCustomModel" in data:
        import aws_sdk_sagemaker.types.bedrock_custom_model_metadata

        out["bedrock_custom_model"] = (
            aws_sdk_sagemaker.types.bedrock_custom_model_metadata.deserialize_aws_json_1_1(
                data["BedrockCustomModel"]
            )
        )
    if "BedrockCustomModelDeployment" in data:
        import aws_sdk_sagemaker.types.bedrock_custom_model_deployment_metadata

        out["bedrock_custom_model_deployment"] = (
            aws_sdk_sagemaker.types.bedrock_custom_model_deployment_metadata.deserialize_aws_json_1_1(
                data["BedrockCustomModelDeployment"]
            )
        )
    if "BedrockProvisionedModelThroughput" in data:
        import aws_sdk_sagemaker.types.bedrock_provisioned_model_throughput_metadata

        out["bedrock_provisioned_model_throughput"] = (
            aws_sdk_sagemaker.types.bedrock_provisioned_model_throughput_metadata.deserialize_aws_json_1_1(
                data["BedrockProvisionedModelThroughput"]
            )
        )
    if "BedrockModelImport" in data:
        import aws_sdk_sagemaker.types.bedrock_model_import_metadata

        out["bedrock_model_import"] = (
            aws_sdk_sagemaker.types.bedrock_model_import_metadata.deserialize_aws_json_1_1(
                data["BedrockModelImport"]
            )
        )
    if "InferenceComponent" in data:
        import aws_sdk_sagemaker.types.inference_component_metadata

        out["inference_component"] = (
            aws_sdk_sagemaker.types.inference_component_metadata.deserialize_aws_json_1_1(
                data["InferenceComponent"]
            )
        )
    if "Lineage" in data:
        import aws_sdk_sagemaker.types.lineage_metadata

        out["lineage"] = (
            aws_sdk_sagemaker.types.lineage_metadata.deserialize_aws_json_1_1(
                data["Lineage"]
            )
        )
    if "Job" in data:
        import aws_sdk_sagemaker.types.job_step_metadata

        out["job"] = aws_sdk_sagemaker.types.job_step_metadata.deserialize_aws_json_1_1(
            data["Job"]
        )
    return out
