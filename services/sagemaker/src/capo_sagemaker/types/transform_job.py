"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_arn
    import capo_sagemaker.types.batch_data_capture_config
    import capo_sagemaker.types.batch_strategy
    import capo_sagemaker.types.data_processing
    import capo_sagemaker.types.experiment_config
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.labeling_job_arn
    import capo_sagemaker.types.max_concurrent_transforms
    import capo_sagemaker.types.max_payload_in_mb
    import capo_sagemaker.types.model_client_config
    import capo_sagemaker.types.model_name
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.transform_environment_map
    import capo_sagemaker.types.transform_input
    import capo_sagemaker.types.transform_job_arn
    import capo_sagemaker.types.transform_job_name
    import capo_sagemaker.types.transform_job_status
    import capo_sagemaker.types.transform_output
    import capo_sagemaker.types.transform_resources


class TransformJob(TypedDict, closed=True):
    transform_job_name: NotRequired[
        "capo_sagemaker.types.transform_job_name.TransformJobName"
    ]
    """<p>The name of the transform job.</p>"""
    transform_job_arn: NotRequired[
        "capo_sagemaker.types.transform_job_arn.TransformJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the transform job.</p>"""
    transform_job_status: NotRequired[
        "capo_sagemaker.types.transform_job_status.TransformJobStatus"
    ]
    """<p>The status of the transform job.</p> <p>Transform job statuses are:</p> <ul> <li> <p> <code>InProgress</code> - The job is in progress.</p> </li> <li> <p> <code>Completed</code> - The job has completed.</p> </li> <li> <p> <code>Failed</code> - The transform job has failed. To see the reason for the failure, see the <code>FailureReason</code> field in the response to a <code>DescribeTransformJob</code> call.</p> </li> <li> <p> <code>Stopping</code> - The transform job is stopping.</p> </li> <li> <p> <code>Stopped</code> - The transform job has stopped.</p> </li> </ul>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the transform job failed, the reason it failed.</p>"""
    model_name: NotRequired["capo_sagemaker.types.model_name.ModelName"]
    """<p>The name of the model associated with the transform job.</p>"""
    max_concurrent_transforms: NotRequired[
        "capo_sagemaker.types.max_concurrent_transforms.MaxConcurrentTransforms"
    ]
    """<p>The maximum number of parallel requests that can be sent to each instance in a transform job. If <code>MaxConcurrentTransforms</code> is set to 0 or left unset, SageMaker checks the optional execution-parameters to determine the settings for your chosen algorithm. If the execution-parameters endpoint is not enabled, the default value is 1. For built-in algorithms, you don't need to set a value for <code>MaxConcurrentTransforms</code>.</p>"""
    model_client_config: NotRequired[
        "capo_sagemaker.types.model_client_config.ModelClientConfig"
    ]
    max_payload_in_mb: NotRequired[
        "capo_sagemaker.types.max_payload_in_mb.MaxPayloadInMB"
    ]
    """<p>The maximum allowed size of the payload, in MB. A payload is the data portion of a record (without metadata). The value in <code>MaxPayloadInMB</code> must be greater than, or equal to, the size of a single record. To estimate the size of a record in MB, divide the size of your dataset by the number of records. To ensure that the records fit within the maximum payload size, we recommend using a slightly larger value. The default value is 6 MB. For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to 0. This feature works only in supported algorithms. Currently, SageMaker built-in algorithms do not support HTTP chunked encoding.</p>"""
    batch_strategy: NotRequired["capo_sagemaker.types.batch_strategy.BatchStrategy"]
    """<p>Specifies the number of records to include in a mini-batch for an HTTP inference request. A record is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.transform_environment_map.TransformEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.</p>"""
    transform_input: NotRequired["capo_sagemaker.types.transform_input.TransformInput"]
    transform_output: NotRequired[
        "capo_sagemaker.types.transform_output.TransformOutput"
    ]
    data_capture_config: NotRequired[
        "capo_sagemaker.types.batch_data_capture_config.BatchDataCaptureConfig"
    ]
    transform_resources: NotRequired[
        "capo_sagemaker.types.transform_resources.TransformResources"
    ]
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the transform Job was created.</p>"""
    transform_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of <code>TransformEndTime</code>.</p>"""
    transform_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of <code>TransformStartTime</code>.</p>"""
    labeling_job_arn: NotRequired[
        "capo_sagemaker.types.labeling_job_arn.LabelingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the labeling job that created the transform job.</p>"""
    auto_ml_job_arn: NotRequired["capo_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The Amazon Resource Name (ARN) of the AutoML job that created the transform job.</p>"""
    data_processing: NotRequired["capo_sagemaker.types.data_processing.DataProcessing"]
    experiment_config: NotRequired[
        "capo_sagemaker.types.experiment_config.ExperimentConfig"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags associated with the transform job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformJob) -> dict:
    out: dict = {}
    if "transform_job_name" in value:
        out["TransformJobName"] = value["transform_job_name"]
    if "transform_job_arn" in value:
        out["TransformJobArn"] = value["transform_job_arn"]
    if "transform_job_status" in value:
        import capo_sagemaker.types.transform_job_status

        out["TransformJobStatus"] = (
            capo_sagemaker.types.transform_job_status.serialize_aws_json_1_1(
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
        import capo_sagemaker.types.model_client_config

        out["ModelClientConfig"] = (
            capo_sagemaker.types.model_client_config.serialize_aws_json_1_1(
                value["model_client_config"]
            )
        )
    if "max_payload_in_mb" in value:
        out["MaxPayloadInMB"] = value["max_payload_in_mb"]
    if "batch_strategy" in value:
        import capo_sagemaker.types.batch_strategy

        out["BatchStrategy"] = (
            capo_sagemaker.types.batch_strategy.serialize_aws_json_1_1(
                value["batch_strategy"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.transform_environment_map

        out["Environment"] = (
            capo_sagemaker.types.transform_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "transform_input" in value:
        import capo_sagemaker.types.transform_input

        out["TransformInput"] = (
            capo_sagemaker.types.transform_input.serialize_aws_json_1_1(
                value["transform_input"]
            )
        )
    if "transform_output" in value:
        import capo_sagemaker.types.transform_output

        out["TransformOutput"] = (
            capo_sagemaker.types.transform_output.serialize_aws_json_1_1(
                value["transform_output"]
            )
        )
    if "data_capture_config" in value:
        import capo_sagemaker.types.batch_data_capture_config

        out["DataCaptureConfig"] = (
            capo_sagemaker.types.batch_data_capture_config.serialize_aws_json_1_1(
                value["data_capture_config"]
            )
        )
    if "transform_resources" in value:
        import capo_sagemaker.types.transform_resources

        out["TransformResources"] = (
            capo_sagemaker.types.transform_resources.serialize_aws_json_1_1(
                value["transform_resources"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "transform_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["TransformStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["transform_start_time"]
            )
        )
    if "transform_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["TransformEndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["transform_end_time"]
        )
    if "labeling_job_arn" in value:
        out["LabelingJobArn"] = value["labeling_job_arn"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "data_processing" in value:
        import capo_sagemaker.types.data_processing

        out["DataProcessing"] = (
            capo_sagemaker.types.data_processing.serialize_aws_json_1_1(
                value["data_processing"]
            )
        )
    if "experiment_config" in value:
        import capo_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            capo_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformJob:
    out: TransformJob = {}  # type: ignore[typeddict-item]
    if "TransformJobName" in data:
        out["transform_job_name"] = data["TransformJobName"]
    if "TransformJobArn" in data:
        out["transform_job_arn"] = data["TransformJobArn"]
    if "TransformJobStatus" in data:
        import capo_sagemaker.types.transform_job_status

        out["transform_job_status"] = (
            capo_sagemaker.types.transform_job_status.deserialize_aws_json_1_1(
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
        import capo_sagemaker.types.model_client_config

        out["model_client_config"] = (
            capo_sagemaker.types.model_client_config.deserialize_aws_json_1_1(
                data["ModelClientConfig"]
            )
        )
    if "MaxPayloadInMB" in data:
        out["max_payload_in_mb"] = data["MaxPayloadInMB"]
    if "BatchStrategy" in data:
        import capo_sagemaker.types.batch_strategy

        out["batch_strategy"] = (
            capo_sagemaker.types.batch_strategy.deserialize_aws_json_1_1(
                data["BatchStrategy"]
            )
        )
    if "Environment" in data:
        import capo_sagemaker.types.transform_environment_map

        out["environment"] = (
            capo_sagemaker.types.transform_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "TransformInput" in data:
        import capo_sagemaker.types.transform_input

        out["transform_input"] = (
            capo_sagemaker.types.transform_input.deserialize_aws_json_1_1(
                data["TransformInput"]
            )
        )
    if "TransformOutput" in data:
        import capo_sagemaker.types.transform_output

        out["transform_output"] = (
            capo_sagemaker.types.transform_output.deserialize_aws_json_1_1(
                data["TransformOutput"]
            )
        )
    if "DataCaptureConfig" in data:
        import capo_sagemaker.types.batch_data_capture_config

        out["data_capture_config"] = (
            capo_sagemaker.types.batch_data_capture_config.deserialize_aws_json_1_1(
                data["DataCaptureConfig"]
            )
        )
    if "TransformResources" in data:
        import capo_sagemaker.types.transform_resources

        out["transform_resources"] = (
            capo_sagemaker.types.transform_resources.deserialize_aws_json_1_1(
                data["TransformResources"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "TransformStartTime" in data:
        import capo_sagemaker.types.timestamp

        out["transform_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TransformStartTime"]
            )
        )
    if "TransformEndTime" in data:
        import capo_sagemaker.types.timestamp

        out["transform_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TransformEndTime"]
            )
        )
    if "LabelingJobArn" in data:
        out["labeling_job_arn"] = data["LabelingJobArn"]
    if "AutoMLJobArn" in data:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if "DataProcessing" in data:
        import capo_sagemaker.types.data_processing

        out["data_processing"] = (
            capo_sagemaker.types.data_processing.deserialize_aws_json_1_1(
                data["DataProcessing"]
            )
        )
    if "ExperimentConfig" in data:
        import capo_sagemaker.types.experiment_config

        out["experiment_config"] = (
            capo_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
