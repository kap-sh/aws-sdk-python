"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3Input``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.processing_local_path
    import aws_sdk_sagemaker.types.processing_s3_compression_type
    import aws_sdk_sagemaker.types.processing_s3_data_distribution_type
    import aws_sdk_sagemaker.types.processing_s3_data_type
    import aws_sdk_sagemaker.types.processing_s3_input_mode
    import aws_sdk_sagemaker.types.s3_uri


class ProcessingS3Input(TypedDict, closed=True):
    s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The URI of the Amazon S3 prefix Amazon SageMaker downloads data required to run a processing job.</p>"""
    local_path: NotRequired[
        "aws_sdk_sagemaker.types.processing_local_path.ProcessingLocalPath"
    ]
    """<p>The local path in your container where you want Amazon SageMaker to write input data to. <code>LocalPath</code> is an absolute path to the input data and must begin with <code>/opt/ml/processing/</code>. <code>LocalPath</code> is a required parameter when <code>AppManaged</code> is <code>False</code> (default).</p>"""
    s3_data_type: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_data_type.ProcessingS3DataType"
    ]
    """<p>Whether you use an <code>S3Prefix</code> or a <code>ManifestFile</code> for the data type. If you choose <code>S3Prefix</code>, <code>S3Uri</code> identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for the processing job. If you choose <code>ManifestFile</code>, <code>S3Uri</code> identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for the processing job.</p>"""
    s3_input_mode: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_input_mode.ProcessingS3InputMode"
    ]
    """<p>Whether to use <code>File</code> or <code>Pipe</code> input mode. In File mode, Amazon SageMaker copies the data from the input source onto the local ML storage volume before starting your processing container. This is the most commonly used input mode. In <code>Pipe</code> mode, Amazon SageMaker streams input data from the source directly to your processing container into named pipes without using the ML storage volume.</p>"""
    s3_data_distribution_type: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_data_distribution_type.ProcessingS3DataDistributionType"
    ]
    """<p>Whether to distribute the data from Amazon S3 to all processing instances with <code>FullyReplicated</code>, or whether the data from Amazon S3 is sharded by Amazon S3 key, downloading one shard of data to each processing instance.</p>"""
    s3_compression_type: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_compression_type.ProcessingS3CompressionType"
    ]
    """<p>Whether to GZIP-decompress the data in Amazon S3 as it is streamed into the processing container. <code>Gzip</code> can only be used when <code>Pipe</code> mode is specified as the <code>S3InputMode</code>. In <code>Pipe</code> mode, Amazon SageMaker streams input data from the source directly to your container without using the EBS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingS3Input) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "s3_data_type" in value:
        import aws_sdk_sagemaker.types.processing_s3_data_type

        out["S3DataType"] = (
            aws_sdk_sagemaker.types.processing_s3_data_type.serialize_aws_json_1_1(
                value["s3_data_type"]
            )
        )
    if "s3_input_mode" in value:
        import aws_sdk_sagemaker.types.processing_s3_input_mode

        out["S3InputMode"] = (
            aws_sdk_sagemaker.types.processing_s3_input_mode.serialize_aws_json_1_1(
                value["s3_input_mode"]
            )
        )
    if "s3_data_distribution_type" in value:
        import aws_sdk_sagemaker.types.processing_s3_data_distribution_type

        out["S3DataDistributionType"] = (
            aws_sdk_sagemaker.types.processing_s3_data_distribution_type.serialize_aws_json_1_1(
                value["s3_data_distribution_type"]
            )
        )
    if "s3_compression_type" in value:
        import aws_sdk_sagemaker.types.processing_s3_compression_type

        out["S3CompressionType"] = (
            aws_sdk_sagemaker.types.processing_s3_compression_type.serialize_aws_json_1_1(
                value["s3_compression_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingS3Input:
    out: ProcessingS3Input = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    if "S3DataType" in data:
        import aws_sdk_sagemaker.types.processing_s3_data_type

        out["s3_data_type"] = (
            aws_sdk_sagemaker.types.processing_s3_data_type.deserialize_aws_json_1_1(
                data["S3DataType"]
            )
        )
    if "S3InputMode" in data:
        import aws_sdk_sagemaker.types.processing_s3_input_mode

        out["s3_input_mode"] = (
            aws_sdk_sagemaker.types.processing_s3_input_mode.deserialize_aws_json_1_1(
                data["S3InputMode"]
            )
        )
    if "S3DataDistributionType" in data:
        import aws_sdk_sagemaker.types.processing_s3_data_distribution_type

        out["s3_data_distribution_type"] = (
            aws_sdk_sagemaker.types.processing_s3_data_distribution_type.deserialize_aws_json_1_1(
                data["S3DataDistributionType"]
            )
        )
    if "S3CompressionType" in data:
        import aws_sdk_sagemaker.types.processing_s3_compression_type

        out["s3_compression_type"] = (
            aws_sdk_sagemaker.types.processing_s3_compression_type.deserialize_aws_json_1_1(
                data["S3CompressionType"]
            )
        )
    return out
