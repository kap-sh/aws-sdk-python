"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobSnsDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.sns_topic_arn


class LabelingJobSnsDataSource(TypedDict):
    sns_topic_arn: NotRequired["aws_sdk_sagemaker.types.sns_topic_arn.SnsTopicArn"]
    """<p>The Amazon SNS input topic Amazon Resource Name (ARN). Specify the ARN of the input topic you will use to send new data objects to a streaming labeling job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobSnsDataSource) -> dict:
    out: dict = {}
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobSnsDataSource:
    out: LabelingJobSnsDataSource = {}  # type: ignore[typeddict-item]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    return out
