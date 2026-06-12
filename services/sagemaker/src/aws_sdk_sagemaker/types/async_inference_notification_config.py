"""Generated from Smithy shape ``com.amazonaws.sagemaker#AsyncInferenceNotificationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.async_notification_topic_type_list
    import aws_sdk_sagemaker.types.sns_topic_arn


class AsyncInferenceNotificationConfig(TypedDict):
    success_topic: NotRequired["aws_sdk_sagemaker.types.sns_topic_arn.SnsTopicArn"]
    """<p>Amazon SNS topic to post a notification to when inference completes successfully. If no topic is provided, no notification is sent on success.</p>"""
    error_topic: NotRequired["aws_sdk_sagemaker.types.sns_topic_arn.SnsTopicArn"]
    """<p>Amazon SNS topic to post a notification to when inference fails. If no topic is provided, no notification is sent on failure.</p>"""
    include_inference_response_in: NotRequired[
        "aws_sdk_sagemaker.types.async_notification_topic_type_list.AsyncNotificationTopicTypeList"
    ]
    """<p>The Amazon SNS topics where you want the inference response to be included.</p> <note> <p>The inference response is included only if the response size is less than or equal to 128 KB.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsyncInferenceNotificationConfig) -> dict:
    out: dict = {}
    if "success_topic" in value:
        out["SuccessTopic"] = value["success_topic"]
    if "error_topic" in value:
        out["ErrorTopic"] = value["error_topic"]
    if "include_inference_response_in" in value:
        import aws_sdk_sagemaker.types.async_notification_topic_type_list

        out["IncludeInferenceResponseIn"] = (
            aws_sdk_sagemaker.types.async_notification_topic_type_list.serialize_aws_json_1_1(
                value["include_inference_response_in"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AsyncInferenceNotificationConfig:
    out: AsyncInferenceNotificationConfig = {}  # type: ignore[typeddict-item]
    if "SuccessTopic" in data:
        out["success_topic"] = data["SuccessTopic"]
    if "ErrorTopic" in data:
        out["error_topic"] = data["ErrorTopic"]
    if "IncludeInferenceResponseIn" in data:
        import aws_sdk_sagemaker.types.async_notification_topic_type_list

        out["include_inference_response_in"] = (
            aws_sdk_sagemaker.types.async_notification_topic_type_list.deserialize_aws_json_1_1(
                data["IncludeInferenceResponseIn"]
            )
        )
    return out
