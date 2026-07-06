"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIWorkloadInputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_channel_name
    import aws_sdk_sagemaker.types.ai_workload_data_source


class AIWorkloadInputDataConfig(TypedDict, closed=True):
    channel_name: NotRequired["aws_sdk_sagemaker.types.ai_channel_name.AIChannelName"]
    """<p>The logical name for the data channel.</p>"""
    data_source: NotRequired[
        "aws_sdk_sagemaker.types.ai_workload_data_source.AIWorkloadDataSource"
    ]
    """<p>The data source for this channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIWorkloadInputDataConfig) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "data_source" in value:
        import aws_sdk_sagemaker.types.ai_workload_data_source

        out["DataSource"] = (
            aws_sdk_sagemaker.types.ai_workload_data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIWorkloadInputDataConfig:
    out: AIWorkloadInputDataConfig = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "DataSource" in data:
        import aws_sdk_sagemaker.types.ai_workload_data_source

        out["data_source"] = (
            aws_sdk_sagemaker.types.ai_workload_data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    return out
