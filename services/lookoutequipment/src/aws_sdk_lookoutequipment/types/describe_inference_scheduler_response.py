"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeInferenceSchedulerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.data_delay_offset_in_minutes
    import aws_sdk_lookoutequipment.types.data_upload_frequency
    import aws_sdk_lookoutequipment.types.iam_role_arn
    import aws_sdk_lookoutequipment.types.inference_input_configuration
    import aws_sdk_lookoutequipment.types.inference_output_configuration
    import aws_sdk_lookoutequipment.types.inference_scheduler_arn
    import aws_sdk_lookoutequipment.types.inference_scheduler_name
    import aws_sdk_lookoutequipment.types.inference_scheduler_status
    import aws_sdk_lookoutequipment.types.kms_key_arn
    import aws_sdk_lookoutequipment.types.latest_inference_result
    import aws_sdk_lookoutequipment.types.model_arn
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.timestamp


class DescribeInferenceSchedulerResponse(TypedDict):
    model_arn: NotRequired["aws_sdk_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the machine learning model of the inference scheduler being described. </p>"""
    model_name: NotRequired["aws_sdk_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model of the inference scheduler being described. </p>"""
    inference_scheduler_name: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName"
    ]
    """<p>The name of the inference scheduler being described. </p>"""
    inference_scheduler_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_arn.InferenceSchedulerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference scheduler being described. </p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_status.InferenceSchedulerStatus"
    ]
    """<p>Indicates the status of the inference scheduler. </p>"""
    data_delay_offset_in_minutes: NotRequired[
        "aws_sdk_lookoutequipment.types.data_delay_offset_in_minutes.DataDelayOffsetInMinutes"
    ]
    """<p> A period of time (in minutes) by which inference on the data is delayed after the data starts. For instance, if you select an offset delay time of five minutes, inference will not begin on the data until the first data measurement after the five minute mark. For example, if five minutes is selected, the inference scheduler will wake up at the configured frequency with the additional five minute delay time to check the customer S3 bucket. The customer can upload data at the same frequency and they don't need to stop and restart the scheduler when uploading new data.</p>"""
    data_upload_frequency: NotRequired[
        "aws_sdk_lookoutequipment.types.data_upload_frequency.DataUploadFrequency"
    ]
    """<p>Specifies how often data is uploaded to the source S3 bucket for the input data. This value is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In this example, it starts once every 5 minutes. </p>"""
    created_at: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Specifies the time at which the inference scheduler was created. </p>"""
    updated_at: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Specifies the time at which the inference scheduler was last updated, if it was. </p>"""
    data_input_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_input_configuration.InferenceInputConfiguration"
    ]
    """<p> Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location. </p>"""
    data_output_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_output_configuration.InferenceOutputConfiguration"
    ]
    """<p> Specifies information for the output results for the inference scheduler, including the output S3 location. </p>"""
    role_arn: NotRequired["aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the inference scheduler being described. </p>"""
    server_side_kms_key_id: NotRequired[
        "aws_sdk_lookoutequipment.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>Provides the identifier of the KMS key used to encrypt inference scheduler data by Amazon Lookout for Equipment. </p>"""
    latest_inference_result: NotRequired[
        "aws_sdk_lookoutequipment.types.latest_inference_result.LatestInferenceResult"
    ]
    """<p>Indicates whether the latest execution for the inference scheduler was Anomalous (anomalous events found) or Normal (no anomalous events found).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeInferenceSchedulerResponse) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "inference_scheduler_name" in value:
        out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "inference_scheduler_arn" in value:
        out["InferenceSchedulerArn"] = value["inference_scheduler_arn"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.inference_scheduler_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.inference_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "data_delay_offset_in_minutes" in value:
        out["DataDelayOffsetInMinutes"] = value["data_delay_offset_in_minutes"]
    if "data_upload_frequency" in value:
        import aws_sdk_lookoutequipment.types.data_upload_frequency

        out["DataUploadFrequency"] = (
            aws_sdk_lookoutequipment.types.data_upload_frequency.serialize_aws_json_1_0(
                value["data_upload_frequency"]
            )
        )
    if "created_at" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["CreatedAt"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["UpdatedAt"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
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
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    if "latest_inference_result" in value:
        import aws_sdk_lookoutequipment.types.latest_inference_result

        out["LatestInferenceResult"] = (
            aws_sdk_lookoutequipment.types.latest_inference_result.serialize_aws_json_1_0(
                value["latest_inference_result"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeInferenceSchedulerResponse:
    out: DescribeInferenceSchedulerResponse = {}  # type: ignore[typeddict-item]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    if "InferenceSchedulerArn" in data:
        out["inference_scheduler_arn"] = data["InferenceSchedulerArn"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.inference_scheduler_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.inference_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "DataDelayOffsetInMinutes" in data:
        out["data_delay_offset_in_minutes"] = data["DataDelayOffsetInMinutes"]
    if "DataUploadFrequency" in data:
        import aws_sdk_lookoutequipment.types.data_upload_frequency

        out["data_upload_frequency"] = (
            aws_sdk_lookoutequipment.types.data_upload_frequency.deserialize_aws_json_1_0(
                data["DataUploadFrequency"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["created_at"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["updated_at"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
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
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ServerSideKmsKeyId" in data:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if "LatestInferenceResult" in data:
        import aws_sdk_lookoutequipment.types.latest_inference_result

        out["latest_inference_result"] = (
            aws_sdk_lookoutequipment.types.latest_inference_result.deserialize_aws_json_1_0(
                data["LatestInferenceResult"]
            )
        )
    return out
