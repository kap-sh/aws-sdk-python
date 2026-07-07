"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalS3DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.additional_s3_data_source_data_type
    import aws_sdk_sagemaker.types.compression_type
    import aws_sdk_sagemaker.types.s3_uri
    import aws_sdk_sagemaker.types.string


class AdditionalS3DataSource(TypedDict, closed=True):
    s3_data_type: NotRequired[
        "aws_sdk_sagemaker.types.additional_s3_data_source_data_type.AdditionalS3DataSourceDataType"
    ]
    """<p>The data type of the additional data source that you specify for use in inference or training. </p>"""
    s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The uniform resource identifier (URI) used to identify an additional data source used in inference or training.</p>"""
    compression_type: NotRequired[
        "aws_sdk_sagemaker.types.compression_type.CompressionType"
    ]
    """<p>The type of compression used for an additional data source used in inference or training. Specify <code>None</code> if your additional data source is not compressed.</p>"""
    e_tag: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The ETag associated with S3 URI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalS3DataSource) -> dict:
    out: dict = {}
    if "s3_data_type" in value:
        import aws_sdk_sagemaker.types.additional_s3_data_source_data_type

        out["S3DataType"] = (
            aws_sdk_sagemaker.types.additional_s3_data_source_data_type.serialize_aws_json_1_1(
                value["s3_data_type"]
            )
        )
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "compression_type" in value:
        import aws_sdk_sagemaker.types.compression_type

        out["CompressionType"] = (
            aws_sdk_sagemaker.types.compression_type.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalS3DataSource:
    out: AdditionalS3DataSource = {}  # type: ignore[typeddict-item]
    if "S3DataType" in data:
        import aws_sdk_sagemaker.types.additional_s3_data_source_data_type

        out["s3_data_type"] = (
            aws_sdk_sagemaker.types.additional_s3_data_source_data_type.deserialize_aws_json_1_1(
                data["S3DataType"]
            )
        )
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    if "CompressionType" in data:
        import aws_sdk_sagemaker.types.compression_type

        out["compression_type"] = (
            aws_sdk_sagemaker.types.compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    return out
