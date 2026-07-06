"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.labeling_job_s3_data_source
    import aws_sdk_sagemaker.types.labeling_job_sns_data_source


class LabelingJobDataSource(TypedDict, closed=True):
    s3_data_source: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_s3_data_source.LabelingJobS3DataSource"
    ]
    """<p>The Amazon S3 location of the input data objects.</p>"""
    sns_data_source: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_sns_data_source.LabelingJobSnsDataSource"
    ]
    r"""<p>An Amazon SNS data source used for streaming labeling jobs. To learn more, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html#sms-streaming-how-it-works-send-data\">Send Data to a Streaming Labeling Job</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobDataSource) -> dict:
    out: dict = {}
    if "s3_data_source" in value:
        import aws_sdk_sagemaker.types.labeling_job_s3_data_source

        out["S3DataSource"] = (
            aws_sdk_sagemaker.types.labeling_job_s3_data_source.serialize_aws_json_1_1(
                value["s3_data_source"]
            )
        )
    if "sns_data_source" in value:
        import aws_sdk_sagemaker.types.labeling_job_sns_data_source

        out["SnsDataSource"] = (
            aws_sdk_sagemaker.types.labeling_job_sns_data_source.serialize_aws_json_1_1(
                value["sns_data_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobDataSource:
    out: LabelingJobDataSource = {}  # type: ignore[typeddict-item]
    if "S3DataSource" in data:
        import aws_sdk_sagemaker.types.labeling_job_s3_data_source

        out["s3_data_source"] = (
            aws_sdk_sagemaker.types.labeling_job_s3_data_source.deserialize_aws_json_1_1(
                data["S3DataSource"]
            )
        )
    if "SnsDataSource" in data:
        import aws_sdk_sagemaker.types.labeling_job_sns_data_source

        out["sns_data_source"] = (
            aws_sdk_sagemaker.types.labeling_job_sns_data_source.deserialize_aws_json_1_1(
                data["SnsDataSource"]
            )
        )
    return out
