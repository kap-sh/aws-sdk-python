"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.bounded_length_string
    import aws_sdk_lookoutequipment.types.inference_execution_status
    import aws_sdk_lookoutequipment.types.inference_input_configuration
    import aws_sdk_lookoutequipment.types.inference_output_configuration
    import aws_sdk_lookoutequipment.types.inference_scheduler_arn
    import aws_sdk_lookoutequipment.types.inference_scheduler_name
    import aws_sdk_lookoutequipment.types.model_arn
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_version
    import aws_sdk_lookoutequipment.types.model_version_arn
    import aws_sdk_lookoutequipment.types.s3_object
    import aws_sdk_lookoutequipment.types.timestamp


class InferenceExecutionSummary(TypedDict, closed=True):
    model_name: NotRequired["aws_sdk_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model being used for the inference execution. </p>"""
    model_arn: NotRequired["aws_sdk_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the machine learning model used for the inference execution. </p>"""
    inference_scheduler_name: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName"
    ]
    """<p>The name of the inference scheduler being used for the inference execution. </p>"""
    inference_scheduler_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_arn.InferenceSchedulerArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the inference scheduler being used for the inference execution. </p>"""
    scheduled_start_time: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Indicates the start time at which the inference scheduler began the specific inference execution. </p>"""
    data_start_time: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the time reference in the dataset at which the inference execution began. </p>"""
    data_end_time: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the time reference in the dataset at which the inference execution stopped. </p>"""
    data_input_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_input_configuration.InferenceInputConfiguration"
    ]
    """<p> Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location. </p>"""
    data_output_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_output_configuration.InferenceOutputConfiguration"
    ]
    """<p> Specifies configuration information for the output results from for the inference execution, including the output Amazon S3 location. </p>"""
    customer_result_object: NotRequired[
        "aws_sdk_lookoutequipment.types.s3_object.S3Object"
    ]
    """<p>The S3 object that the inference execution results were uploaded to.</p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_execution_status.InferenceExecutionStatus"
    ]
    """<p>Indicates the status of the inference execution. </p>"""
    failed_reason: NotRequired[
        "aws_sdk_lookoutequipment.types.bounded_length_string.BoundedLengthString"
    ]
    """<p> Specifies the reason for failure when an inference execution has failed. </p>"""
    model_version: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>The model version used for the inference execution.</p>"""
    model_version_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the model version used for the inference execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceExecutionSummary) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "inference_scheduler_name" in value:
        out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "inference_scheduler_arn" in value:
        out["InferenceSchedulerArn"] = value["inference_scheduler_arn"]
    if "scheduled_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["ScheduledStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["scheduled_start_time"]
            )
        )
    if "data_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["DataStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_start_time"]
            )
        )
    if "data_end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["DataEndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_end_time"]
            )
        )
    if "data_input_configuration" in value:
        import aws_sdk_lookoutequipment.types.inference_input_configuration

        out["DataInputConfiguration"] = (
            aws_sdk_lookoutequipment.types.inference_input_configuration.serialize_aws_json_1_0(
                value["data_input_configuration"]
            )
        )
    if "data_output_configuration" in value:
        import aws_sdk_lookoutequipment.types.inference_output_configuration

        out["DataOutputConfiguration"] = (
            aws_sdk_lookoutequipment.types.inference_output_configuration.serialize_aws_json_1_0(
                value["data_output_configuration"]
            )
        )
    if "customer_result_object" in value:
        import aws_sdk_lookoutequipment.types.s3_object

        out["CustomerResultObject"] = (
            aws_sdk_lookoutequipment.types.s3_object.serialize_aws_json_1_0(
                value["customer_result_object"]
            )
        )
    if "status" in value:
        import aws_sdk_lookoutequipment.types.inference_execution_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.inference_execution_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "failed_reason" in value:
        out["FailedReason"] = value["failed_reason"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "model_version_arn" in value:
        out["ModelVersionArn"] = value["model_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InferenceExecutionSummary:
    out: InferenceExecutionSummary = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    if "InferenceSchedulerArn" in data:
        out["inference_scheduler_arn"] = data["InferenceSchedulerArn"]
    if "ScheduledStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["scheduled_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["ScheduledStartTime"]
            )
        )
    if "DataStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["data_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataStartTime"]
            )
        )
    if "DataEndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["data_end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataEndTime"]
            )
        )
    if "DataInputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.inference_input_configuration

        out["data_input_configuration"] = (
            aws_sdk_lookoutequipment.types.inference_input_configuration.deserialize_aws_json_1_0(
                data["DataInputConfiguration"]
            )
        )
    if "DataOutputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.inference_output_configuration

        out["data_output_configuration"] = (
            aws_sdk_lookoutequipment.types.inference_output_configuration.deserialize_aws_json_1_0(
                data["DataOutputConfiguration"]
            )
        )
    if "CustomerResultObject" in data:
        import aws_sdk_lookoutequipment.types.s3_object

        out["customer_result_object"] = (
            aws_sdk_lookoutequipment.types.s3_object.deserialize_aws_json_1_0(
                data["CustomerResultObject"]
            )
        )
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.inference_execution_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.inference_execution_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "FailedReason" in data:
        out["failed_reason"] = data["FailedReason"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "ModelVersionArn" in data:
        out["model_version_arn"] = data["ModelVersionArn"]
    return out
