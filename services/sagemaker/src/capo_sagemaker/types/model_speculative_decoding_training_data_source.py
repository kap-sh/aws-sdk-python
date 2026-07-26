"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSpeculativeDecodingTrainingDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_speculative_decoding_s3_data_type
    import capo_sagemaker.types.s3_uri


class ModelSpeculativeDecodingTrainingDataSource(TypedDict, closed=True):
    s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI that points to the training data for speculative decoding.</p>"""
    s3_data_type: NotRequired[
        "capo_sagemaker.types.model_speculative_decoding_s3_data_type.ModelSpeculativeDecodingS3DataType"
    ]
    """<p>The type of data stored in the Amazon S3 location. Valid values are <code>S3Prefix</code> or <code>ManifestFile</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSpeculativeDecodingTrainingDataSource) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "s3_data_type" in value:
        import capo_sagemaker.types.model_speculative_decoding_s3_data_type

        out["S3DataType"] = (
            capo_sagemaker.types.model_speculative_decoding_s3_data_type.serialize_aws_json_1_1(
                value["s3_data_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelSpeculativeDecodingTrainingDataSource:
    out: ModelSpeculativeDecodingTrainingDataSource = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    if "S3DataType" in data:
        import capo_sagemaker.types.model_speculative_decoding_s3_data_type

        out["s3_data_type"] = (
            capo_sagemaker.types.model_speculative_decoding_s3_data_type.deserialize_aws_json_1_1(
                data["S3DataType"]
            )
        )
    return out
