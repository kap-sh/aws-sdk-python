"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceSchedulerSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.data_delay_offset_in_minutes
    import aws_sdk_lookoutequipment.types.data_upload_frequency
    import aws_sdk_lookoutequipment.types.inference_scheduler_arn
    import aws_sdk_lookoutequipment.types.inference_scheduler_name
    import aws_sdk_lookoutequipment.types.inference_scheduler_status
    import aws_sdk_lookoutequipment.types.latest_inference_result
    import aws_sdk_lookoutequipment.types.model_arn
    import aws_sdk_lookoutequipment.types.model_name


class InferenceSchedulerSummary(TypedDict):
    model_name: NotRequired["aws_sdk_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model used for the inference scheduler. </p>"""
    model_arn: NotRequired["aws_sdk_lookoutequipment.types.model_arn.ModelArn"]
    """<p> The Amazon Resource Name (ARN) of the machine learning model used by the inference scheduler. </p>"""
    inference_scheduler_name: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName"
    ]
    """<p>The name of the inference scheduler. </p>"""
    inference_scheduler_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_arn.InferenceSchedulerArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the inference scheduler. </p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_status.InferenceSchedulerStatus"
    ]
    """<p>Indicates the status of the inference scheduler. </p>"""
    data_delay_offset_in_minutes: NotRequired[
        "aws_sdk_lookoutequipment.types.data_delay_offset_in_minutes.DataDelayOffsetInMinutes"
    ]
    """<p>A period of time (in minutes) by which inference on the data is delayed after the data starts. For instance, if an offset delay time of five minutes was selected, inference will not begin on the data until the first data measurement after the five minute mark. For example, if five minutes is selected, the inference scheduler will wake up at the configured frequency with the additional five minute delay time to check the customer S3 bucket. The customer can upload data at the same frequency and they don't need to stop and restart the scheduler when uploading new data. </p>"""
    data_upload_frequency: NotRequired[
        "aws_sdk_lookoutequipment.types.data_upload_frequency.DataUploadFrequency"
    ]
    """<p>How often data is uploaded to the source S3 bucket for the input data. This value is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In this example, it starts once every 5 minutes. </p>"""
    latest_inference_result: NotRequired[
        "aws_sdk_lookoutequipment.types.latest_inference_result.LatestInferenceResult"
    ]
    """<p>Indicates whether the latest execution for the inference scheduler was Anomalous (anomalous events found) or Normal (no anomalous events found).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceSchedulerSummary) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
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
    if "latest_inference_result" in value:
        import aws_sdk_lookoutequipment.types.latest_inference_result

        out["LatestInferenceResult"] = (
            aws_sdk_lookoutequipment.types.latest_inference_result.serialize_aws_json_1_0(
                value["latest_inference_result"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InferenceSchedulerSummary:
    out: InferenceSchedulerSummary = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
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
    if "LatestInferenceResult" in data:
        import aws_sdk_lookoutequipment.types.latest_inference_result

        out["latest_inference_result"] = (
            aws_sdk_lookoutequipment.types.latest_inference_result.deserialize_aws_json_1_0(
                data["LatestInferenceResult"]
            )
        )
    return out
