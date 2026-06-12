"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationDeploymentS3Channel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_channel_name
    import aws_sdk_sagemaker.types.s3_uri


class AIRecommendationDeploymentS3Channel(TypedDict):
    channel_name: NotRequired["aws_sdk_sagemaker.types.ai_channel_name.AIChannelName"]
    """<p>A custom name for this Amazon S3 data channel.</p>"""
    uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI of the data for this channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationDeploymentS3Channel) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "uri" in value:
        out["Uri"] = value["uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationDeploymentS3Channel:
    out: AIRecommendationDeploymentS3Channel = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    return out
