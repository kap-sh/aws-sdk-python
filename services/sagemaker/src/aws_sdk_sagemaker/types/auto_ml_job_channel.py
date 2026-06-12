"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobChannel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_channel_type
    import aws_sdk_sagemaker.types.auto_ml_data_source
    import aws_sdk_sagemaker.types.compression_type
    import aws_sdk_sagemaker.types.content_type


class AutoMLJobChannel(TypedDict):
    channel_type: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_channel_type.AutoMLChannelType"
    ]
    """<p>The type of channel. Defines whether the data are used for training or validation. The default value is <code>training</code>. Channels for <code>training</code> and <code>validation</code> must share the same <code>ContentType</code> </p> <note> <p>The type of channel defaults to <code>training</code> for the time-series forecasting problem type.</p> </note>"""
    content_type: NotRequired["aws_sdk_sagemaker.types.content_type.ContentType"]
    """<p>The content type of the data from the input source. The following are the allowed content types for different problems:</p> <ul> <li> <p>For tabular problem types: <code>text/csv;header=present</code> or <code>x-application/vnd.amazon+parquet</code>. The default value is <code>text/csv;header=present</code>.</p> </li> <li> <p>For image classification: <code>image/png</code>, <code>image/jpeg</code>, or <code>image/*</code>. The default value is <code>image/*</code>.</p> </li> <li> <p>For text classification: <code>text/csv;header=present</code> or <code>x-application/vnd.amazon+parquet</code>. The default value is <code>text/csv;header=present</code>.</p> </li> <li> <p>For time-series forecasting: <code>text/csv;header=present</code> or <code>x-application/vnd.amazon+parquet</code>. The default value is <code>text/csv;header=present</code>.</p> </li> <li> <p>For text generation (LLMs fine-tuning): <code>text/csv;header=present</code> or <code>x-application/vnd.amazon+parquet</code>. The default value is <code>text/csv;header=present</code>.</p> </li> </ul>"""
    compression_type: NotRequired[
        "aws_sdk_sagemaker.types.compression_type.CompressionType"
    ]
    """<p>The allowed compression types depend on the input format and problem type. We allow the compression type <code>Gzip</code> for <code>S3Prefix</code> inputs on tabular data only. For all other inputs, the compression type should be <code>None</code>. If no compression type is provided, we default to <code>None</code>.</p>"""
    data_source: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_data_source.AutoMLDataSource"
    ]
    """<p>The data source for an AutoML channel (Required).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobChannel) -> dict:
    out: dict = {}
    if "channel_type" in value:
        import aws_sdk_sagemaker.types.auto_ml_channel_type

        out["ChannelType"] = (
            aws_sdk_sagemaker.types.auto_ml_channel_type.serialize_aws_json_1_1(
                value["channel_type"]
            )
        )
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "compression_type" in value:
        import aws_sdk_sagemaker.types.compression_type

        out["CompressionType"] = (
            aws_sdk_sagemaker.types.compression_type.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    if "data_source" in value:
        import aws_sdk_sagemaker.types.auto_ml_data_source

        out["DataSource"] = (
            aws_sdk_sagemaker.types.auto_ml_data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLJobChannel:
    out: AutoMLJobChannel = {}  # type: ignore[typeddict-item]
    if "ChannelType" in data:
        import aws_sdk_sagemaker.types.auto_ml_channel_type

        out["channel_type"] = (
            aws_sdk_sagemaker.types.auto_ml_channel_type.deserialize_aws_json_1_1(
                data["ChannelType"]
            )
        )
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    if "CompressionType" in data:
        import aws_sdk_sagemaker.types.compression_type

        out["compression_type"] = (
            aws_sdk_sagemaker.types.compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    if "DataSource" in data:
        import aws_sdk_sagemaker.types.auto_ml_data_source

        out["data_source"] = (
            aws_sdk_sagemaker.types.auto_ml_data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    return out
