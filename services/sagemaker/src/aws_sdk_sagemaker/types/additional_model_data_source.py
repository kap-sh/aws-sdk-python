"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalModelDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.additional_model_channel_name
    import aws_sdk_sagemaker.types.s3_model_data_source


class AdditionalModelDataSource(TypedDict, closed=True):
    channel_name: NotRequired[
        "aws_sdk_sagemaker.types.additional_model_channel_name.AdditionalModelChannelName"
    ]
    """<p>A custom name for this <code>AdditionalModelDataSource</code> object.</p>"""
    s3_data_source: NotRequired[
        "aws_sdk_sagemaker.types.s3_model_data_source.S3ModelDataSource"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalModelDataSource) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "s3_data_source" in value:
        import aws_sdk_sagemaker.types.s3_model_data_source

        out["S3DataSource"] = (
            aws_sdk_sagemaker.types.s3_model_data_source.serialize_aws_json_1_1(
                value["s3_data_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalModelDataSource:
    out: AdditionalModelDataSource = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "S3DataSource" in data:
        import aws_sdk_sagemaker.types.s3_model_data_source

        out["s3_data_source"] = (
            aws_sdk_sagemaker.types.s3_model_data_source.deserialize_aws_json_1_1(
                data["S3DataSource"]
            )
        )
    return out
