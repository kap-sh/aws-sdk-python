"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_managed
    import aws_sdk_sagemaker.types.processing_feature_store_output
    import aws_sdk_sagemaker.types.processing_s3_output
    import aws_sdk_sagemaker.types.string


class ProcessingOutput(TypedDict):
    output_name: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name for the processing job output.</p>"""
    s3_output: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_output.ProcessingS3Output"
    ]
    """<p>Configuration for processing job outputs in Amazon S3.</p>"""
    feature_store_output: NotRequired[
        "aws_sdk_sagemaker.types.processing_feature_store_output.ProcessingFeatureStoreOutput"
    ]
    """<p>Configuration for processing job outputs in Amazon SageMaker Feature Store. This processing output type is only supported when <code>AppManaged</code> is specified. </p>"""
    app_managed: NotRequired["aws_sdk_sagemaker.types.app_managed.AppManaged"]
    """<p>When <code>True</code>, output operations such as data upload are managed natively by the processing job application. When <code>False</code> (default), output operations are managed by Amazon SageMaker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingOutput) -> dict:
    out: dict = {}
    if "output_name" in value:
        out["OutputName"] = value["output_name"]
    if "s3_output" in value:
        import aws_sdk_sagemaker.types.processing_s3_output

        out["S3Output"] = (
            aws_sdk_sagemaker.types.processing_s3_output.serialize_aws_json_1_1(
                value["s3_output"]
            )
        )
    if "feature_store_output" in value:
        import aws_sdk_sagemaker.types.processing_feature_store_output

        out["FeatureStoreOutput"] = (
            aws_sdk_sagemaker.types.processing_feature_store_output.serialize_aws_json_1_1(
                value["feature_store_output"]
            )
        )
    if "app_managed" in value:
        out["AppManaged"] = value["app_managed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingOutput:
    out: ProcessingOutput = {}  # type: ignore[typeddict-item]
    if "OutputName" in data:
        out["output_name"] = data["OutputName"]
    if "S3Output" in data:
        import aws_sdk_sagemaker.types.processing_s3_output

        out["s3_output"] = (
            aws_sdk_sagemaker.types.processing_s3_output.deserialize_aws_json_1_1(
                data["S3Output"]
            )
        )
    if "FeatureStoreOutput" in data:
        import aws_sdk_sagemaker.types.processing_feature_store_output

        out["feature_store_output"] = (
            aws_sdk_sagemaker.types.processing_feature_store_output.deserialize_aws_json_1_1(
                data["FeatureStoreOutput"]
            )
        )
    if "AppManaged" in data:
        out["app_managed"] = data["AppManaged"]
    return out
