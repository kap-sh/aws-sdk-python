"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.s3_model_data_source


class ModelDataSource(TypedDict):
    s3_data_source: NotRequired[
        "aws_sdk_sagemaker.types.s3_model_data_source.S3ModelDataSource"
    ]
    """<p>Specifies the S3 location of ML model data to deploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDataSource) -> dict:
    out: dict = {}
    if "s3_data_source" in value:
        import aws_sdk_sagemaker.types.s3_model_data_source

        out["S3DataSource"] = (
            aws_sdk_sagemaker.types.s3_model_data_source.serialize_aws_json_1_1(
                value["s3_data_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDataSource:
    out: ModelDataSource = {}  # type: ignore[typeddict-item]
    if "S3DataSource" in data:
        import aws_sdk_sagemaker.types.s3_model_data_source

        out["s3_data_source"] = (
            aws_sdk_sagemaker.types.s3_model_data_source.deserialize_aws_json_1_1(
                data["S3DataSource"]
            )
        )
    return out
