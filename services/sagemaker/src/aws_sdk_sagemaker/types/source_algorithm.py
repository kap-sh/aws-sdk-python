"""Generated from Smithy shape ``com.amazonaws.sagemaker#SourceAlgorithm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.arn_or_name
    import aws_sdk_sagemaker.types.model_data_source
    import aws_sdk_sagemaker.types.string
    import aws_sdk_sagemaker.types.url


class SourceAlgorithm(TypedDict):
    model_data_url: NotRequired["aws_sdk_sagemaker.types.url.Url"]
    """<p>The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single <code>gzip</code> compressed tar archive (<code>.tar.gz</code> suffix).</p> <note> <p>The model artifacts must be in an S3 bucket that is in the same Amazon Web Services region as the algorithm.</p> </note>"""
    model_data_source: NotRequired[
        "aws_sdk_sagemaker.types.model_data_source.ModelDataSource"
    ]
    """<p>Specifies the location of ML model data to deploy during endpoint creation.</p>"""
    model_data_e_tag: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The ETag associated with Model Data URL.</p>"""
    algorithm_name: NotRequired["aws_sdk_sagemaker.types.arn_or_name.ArnOrName"]
    """<p>The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in Amazon Web Services Marketplace that you are subscribed to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAlgorithm) -> dict:
    out: dict = {}
    if "model_data_url" in value:
        out["ModelDataUrl"] = value["model_data_url"]
    if "model_data_source" in value:
        import aws_sdk_sagemaker.types.model_data_source

        out["ModelDataSource"] = (
            aws_sdk_sagemaker.types.model_data_source.serialize_aws_json_1_1(
                value["model_data_source"]
            )
        )
    if "model_data_e_tag" in value:
        out["ModelDataETag"] = value["model_data_e_tag"]
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceAlgorithm:
    out: SourceAlgorithm = {}  # type: ignore[typeddict-item]
    if "ModelDataUrl" in data:
        out["model_data_url"] = data["ModelDataUrl"]
    if "ModelDataSource" in data:
        import aws_sdk_sagemaker.types.model_data_source

        out["model_data_source"] = (
            aws_sdk_sagemaker.types.model_data_source.deserialize_aws_json_1_1(
                data["ModelDataSource"]
            )
        )
    if "ModelDataETag" in data:
        out["model_data_e_tag"] = data["ModelDataETag"]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    return out
