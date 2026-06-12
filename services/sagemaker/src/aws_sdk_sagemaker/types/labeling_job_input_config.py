"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobInputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.labeling_job_data_attributes
    import aws_sdk_sagemaker.types.labeling_job_data_source


class LabelingJobInputConfig(TypedDict):
    data_source: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_data_source.LabelingJobDataSource"
    ]
    """<p>The location of the input data.</p>"""
    data_attributes: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_data_attributes.LabelingJobDataAttributes"
    ]
    """<p>Attributes of the data specified by the customer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobInputConfig) -> dict:
    out: dict = {}
    if "data_source" in value:
        import aws_sdk_sagemaker.types.labeling_job_data_source

        out["DataSource"] = (
            aws_sdk_sagemaker.types.labeling_job_data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "data_attributes" in value:
        import aws_sdk_sagemaker.types.labeling_job_data_attributes

        out["DataAttributes"] = (
            aws_sdk_sagemaker.types.labeling_job_data_attributes.serialize_aws_json_1_1(
                value["data_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobInputConfig:
    out: LabelingJobInputConfig = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import aws_sdk_sagemaker.types.labeling_job_data_source

        out["data_source"] = (
            aws_sdk_sagemaker.types.labeling_job_data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    if "DataAttributes" in data:
        import aws_sdk_sagemaker.types.labeling_job_data_attributes

        out["data_attributes"] = (
            aws_sdk_sagemaker.types.labeling_job_data_attributes.deserialize_aws_json_1_1(
                data["DataAttributes"]
            )
        )
    return out
