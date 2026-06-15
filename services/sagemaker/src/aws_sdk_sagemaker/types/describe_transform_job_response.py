"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTransformJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_arn
    import aws_sdk_sagemaker.types.batch_data_capture_config
    import aws_sdk_sagemaker.types.batch_strategy
    import aws_sdk_sagemaker.types.data_processing
    import aws_sdk_sagemaker.types.experiment_config
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.labeling_job_arn
    import aws_sdk_sagemaker.types.max_concurrent_transforms
    import aws_sdk_sagemaker.types.max_payload_in_mb
    import aws_sdk_sagemaker.types.model_client_config
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.transform_environment_map
    import aws_sdk_sagemaker.types.transform_input
    import aws_sdk_sagemaker.types.transform_job_arn
    import aws_sdk_sagemaker.types.transform_job_name
    import aws_sdk_sagemaker.types.transform_job_status
    import aws_sdk_sagemaker.types.transform_output
    import aws_sdk_sagemaker.types.transform_resources


class DescribeTransformJobResponse(TypedDict):
    transform_job_name: NotRequired[
        "aws_sdk_sagemaker.types.transform_job_name.TransformJobName"
    ]
    """<p>The name of the transform job.</p>"""
    transform_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.transform_job_arn.TransformJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the transform job.</p>"""
    transform_job_status: NotRequired[
        "aws_sdk_sagemaker.types.transform_job_status.TransformJobStatus"
    ]
    """<p>The status of the transform job. If the transform job failed, the reason is returned in the <code>FailureReason</code> field.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    r"""<p>If the transform job failed, <code>FailureReason</code> describes why it failed. A transform job creates a log file, which includes error messages, and stores it as an Amazon S3 object. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html\">Log Amazon SageMaker Events with Amazon CloudWatch</a>.</p>"""
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of the model used in the transform job.</p>"""
    max_concurrent_transforms: NotRequired[
        "aws_sdk_sagemaker.types.max_concurrent_transforms.MaxConcurrentTransforms"
    ]
    """<p>The maximum number of parallel requests on each instance node that can be launched in a transform job. The default value is 1.</p>"""
    model_client_config: NotRequired[
        "aws_sdk_sagemaker.types.model_client_config.ModelClientConfig"
    ]
    """<p>The timeout and maximum number of retries for processing a transform job invocation.</p>"""
    max_payload_in_mb: NotRequired[
        "aws_sdk_sagemaker.types.max_payload_in_mb.MaxPayloadInMB"
    ]
    """<p>The maximum payload size, in MB, used in the transform job.</p>"""
    batch_strategy: NotRequired["aws_sdk_sagemaker.types.batch_strategy.BatchStrategy"]
    """<p>Specifies the number of records to include in a mini-batch for an HTTP inference request. A <i>record</i> <i/> is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record. </p> <p>To enable the batch strategy, you must set <code>SplitType</code> to <code>Line</code>, <code>RecordIO</code>, or <code>TFRecord</code>.</p>"""
    environment: NotRequired[
        "aws_sdk_sagemaker.types.transform_environment_map.TransformEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.</p>"""
    transform_input: NotRequired[
        "aws_sdk_sagemaker.types.transform_input.TransformInput"
    ]
    """<p>Describes the dataset to be transformed and the Amazon S3 location where it is stored.</p>"""
    transform_output: NotRequired[
        "aws_sdk_sagemaker.types.transform_output.TransformOutput"
    ]
    """<p>Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.</p>"""
    data_capture_config: NotRequired[
        "aws_sdk_sagemaker.types.batch_data_capture_config.BatchDataCaptureConfig"
    ]
    """<p>Configuration to control how SageMaker captures inference data.</p>"""
    transform_resources: NotRequired[
        "aws_sdk_sagemaker.types.transform_resources.TransformResources"
    ]
    """<p>Describes the resources, including ML instance types and ML instance count, to use for the transform job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the transform Job was created.</p>"""
    transform_start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of <code>TransformEndTime</code>.</p>"""
    transform_end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of <code>TransformStartTime</code>.</p>"""
    labeling_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_arn.LabelingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon SageMaker Ground Truth labeling job that created the transform or training job.</p>"""
    auto_ml_job_arn: NotRequired["aws_sdk_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The Amazon Resource Name (ARN) of the AutoML transform job.</p>"""
    data_processing: NotRequired[
        "aws_sdk_sagemaker.types.data_processing.DataProcessing"
    ]
    experiment_config: NotRequired[
        "aws_sdk_sagemaker.types.experiment_config.ExperimentConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTransformJobResponse) -> dict:
    out: dict = {}
    if "transform_job_name" in value:
        out["TransformJobName"] = value["transform_job_name"]
    if "transform_job_arn" in value:
        out["TransformJobArn"] = value["transform_job_arn"]
    if "transform_job_status" in value:
        import aws_sdk_sagemaker.types.transform_job_status

        out["TransformJobStatus"] = (
            aws_sdk_sagemaker.types.transform_job_status.serialize_aws_json_1_1(
                value["transform_job_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "max_concurrent_transforms" in value:
        out["MaxConcurrentTransforms"] = value["max_concurrent_transforms"]
    if "model_client_config" in value:
        import aws_sdk_sagemaker.types.model_client_config

        out["ModelClientConfig"] = (
            aws_sdk_sagemaker.types.model_client_config.serialize_aws_json_1_1(
                value["model_client_config"]
            )
        )
    if "max_payload_in_mb" in value:
        out["MaxPayloadInMB"] = value["max_payload_in_mb"]
    if "batch_strategy" in value:
        import aws_sdk_sagemaker.types.batch_strategy

        out["BatchStrategy"] = (
            aws_sdk_sagemaker.types.batch_strategy.serialize_aws_json_1_1(
                value["batch_strategy"]
            )
        )
    if "environment" in value:
        import aws_sdk_sagemaker.types.transform_environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.transform_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "transform_input" in value:
        import aws_sdk_sagemaker.types.transform_input

        out["TransformInput"] = (
            aws_sdk_sagemaker.types.transform_input.serialize_aws_json_1_1(
                value["transform_input"]
            )
        )
    if "transform_output" in value:
        import aws_sdk_sagemaker.types.transform_output

        out["TransformOutput"] = (
            aws_sdk_sagemaker.types.transform_output.serialize_aws_json_1_1(
                value["transform_output"]
            )
        )
    if "data_capture_config" in value:
        import aws_sdk_sagemaker.types.batch_data_capture_config

        out["DataCaptureConfig"] = (
            aws_sdk_sagemaker.types.batch_data_capture_config.serialize_aws_json_1_1(
                value["data_capture_config"]
            )
        )
    if "transform_resources" in value:
        import aws_sdk_sagemaker.types.transform_resources

        out["TransformResources"] = (
            aws_sdk_sagemaker.types.transform_resources.serialize_aws_json_1_1(
                value["transform_resources"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "transform_start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["TransformStartTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["transform_start_time"]
            )
        )
    if "transform_end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["TransformEndTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["transform_end_time"]
            )
        )
    if "labeling_job_arn" in value:
        out["LabelingJobArn"] = value["labeling_job_arn"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "data_processing" in value:
        import aws_sdk_sagemaker.types.data_processing

        out["DataProcessing"] = (
            aws_sdk_sagemaker.types.data_processing.serialize_aws_json_1_1(
                value["data_processing"]
            )
        )
    if "experiment_config" in value:
        import aws_sdk_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            aws_sdk_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTransformJobResponse:
    out: DescribeTransformJobResponse = {}  # type: ignore[typeddict-item]
    if "TransformJobName" in data:
        out["transform_job_name"] = data["TransformJobName"]
    if "TransformJobArn" in data:
        out["transform_job_arn"] = data["TransformJobArn"]
    if "TransformJobStatus" in data:
        import aws_sdk_sagemaker.types.transform_job_status

        out["transform_job_status"] = (
            aws_sdk_sagemaker.types.transform_job_status.deserialize_aws_json_1_1(
                data["TransformJobStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "MaxConcurrentTransforms" in data:
        out["max_concurrent_transforms"] = data["MaxConcurrentTransforms"]
    if "ModelClientConfig" in data:
        import aws_sdk_sagemaker.types.model_client_config

        out["model_client_config"] = (
            aws_sdk_sagemaker.types.model_client_config.deserialize_aws_json_1_1(
                data["ModelClientConfig"]
            )
        )
    if "MaxPayloadInMB" in data:
        out["max_payload_in_mb"] = data["MaxPayloadInMB"]
    if "BatchStrategy" in data:
        import aws_sdk_sagemaker.types.batch_strategy

        out["batch_strategy"] = (
            aws_sdk_sagemaker.types.batch_strategy.deserialize_aws_json_1_1(
                data["BatchStrategy"]
            )
        )
    if "Environment" in data:
        import aws_sdk_sagemaker.types.transform_environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.transform_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "TransformInput" in data:
        import aws_sdk_sagemaker.types.transform_input

        out["transform_input"] = (
            aws_sdk_sagemaker.types.transform_input.deserialize_aws_json_1_1(
                data["TransformInput"]
            )
        )
    if "TransformOutput" in data:
        import aws_sdk_sagemaker.types.transform_output

        out["transform_output"] = (
            aws_sdk_sagemaker.types.transform_output.deserialize_aws_json_1_1(
                data["TransformOutput"]
            )
        )
    if "DataCaptureConfig" in data:
        import aws_sdk_sagemaker.types.batch_data_capture_config

        out["data_capture_config"] = (
            aws_sdk_sagemaker.types.batch_data_capture_config.deserialize_aws_json_1_1(
                data["DataCaptureConfig"]
            )
        )
    if "TransformResources" in data:
        import aws_sdk_sagemaker.types.transform_resources

        out["transform_resources"] = (
            aws_sdk_sagemaker.types.transform_resources.deserialize_aws_json_1_1(
                data["TransformResources"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "TransformStartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["transform_start_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TransformStartTime"]
            )
        )
    if "TransformEndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["transform_end_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TransformEndTime"]
            )
        )
    if "LabelingJobArn" in data:
        out["labeling_job_arn"] = data["LabelingJobArn"]
    if "AutoMLJobArn" in data:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if "DataProcessing" in data:
        import aws_sdk_sagemaker.types.data_processing

        out["data_processing"] = (
            aws_sdk_sagemaker.types.data_processing.deserialize_aws_json_1_1(
                data["DataProcessing"]
            )
        )
    if "ExperimentConfig" in data:
        import aws_sdk_sagemaker.types.experiment_config

        out["experiment_config"] = (
            aws_sdk_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    return out
