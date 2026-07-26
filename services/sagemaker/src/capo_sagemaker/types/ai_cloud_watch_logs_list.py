"""Generated from Smithy shape ``com.amazonaws.sagemaker#AICloudWatchLogsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_cloud_watch_logs

AICloudWatchLogsList: TypeAlias = list[
    "capo_sagemaker.types.ai_cloud_watch_logs.AICloudWatchLogs"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AICloudWatchLogsList) -> list:
    import capo_sagemaker.types.ai_cloud_watch_logs

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_cloud_watch_logs.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AICloudWatchLogsList:
    import capo_sagemaker.types.ai_cloud_watch_logs

    out: AICloudWatchLogsList = []
    for item in data:
        out.append(
            capo_sagemaker.types.ai_cloud_watch_logs.deserialize_aws_json_1_1(item)
        )
    return out
