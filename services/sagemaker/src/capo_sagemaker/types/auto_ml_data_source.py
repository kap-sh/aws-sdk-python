"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_mls3_data_source


class AutoMLDataSource(TypedDict, closed=True):
    s3_data_source: NotRequired[
        "capo_sagemaker.types.auto_mls3_data_source.AutoMLS3DataSource"
    ]
    """<p>The Amazon S3 location of the input data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLDataSource) -> dict:
    out: dict = {}
    if "s3_data_source" in value:
        import capo_sagemaker.types.auto_mls3_data_source

        out["S3DataSource"] = (
            capo_sagemaker.types.auto_mls3_data_source.serialize_aws_json_1_1(
                value["s3_data_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLDataSource:
    out: AutoMLDataSource = {}  # type: ignore[typeddict-item]
    if "S3DataSource" in data:
        import capo_sagemaker.types.auto_mls3_data_source

        out["s3_data_source"] = (
            capo_sagemaker.types.auto_mls3_data_source.deserialize_aws_json_1_1(
                data["S3DataSource"]
            )
        )
    return out
