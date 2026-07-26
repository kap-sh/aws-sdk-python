"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.dataset_source
    import capo_sagemaker.types.file_system_data_source
    import capo_sagemaker.types.s3_data_source


class DataSource(TypedDict, closed=True):
    s3_data_source: NotRequired["capo_sagemaker.types.s3_data_source.S3DataSource"]
    """<p>The S3 location of the data source that is associated with a channel.</p>"""
    file_system_data_source: NotRequired[
        "capo_sagemaker.types.file_system_data_source.FileSystemDataSource"
    ]
    """<p>The file system that is associated with a channel.</p>"""
    dataset_source: NotRequired["capo_sagemaker.types.dataset_source.DatasetSource"]
    """<p> The dataset resource that's associated with a channel. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> dict:
    out: dict = {}
    if "s3_data_source" in value:
        import capo_sagemaker.types.s3_data_source

        out["S3DataSource"] = (
            capo_sagemaker.types.s3_data_source.serialize_aws_json_1_1(
                value["s3_data_source"]
            )
        )
    if "file_system_data_source" in value:
        import capo_sagemaker.types.file_system_data_source

        out["FileSystemDataSource"] = (
            capo_sagemaker.types.file_system_data_source.serialize_aws_json_1_1(
                value["file_system_data_source"]
            )
        )
    if "dataset_source" in value:
        import capo_sagemaker.types.dataset_source

        out["DatasetSource"] = (
            capo_sagemaker.types.dataset_source.serialize_aws_json_1_1(
                value["dataset_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "S3DataSource" in data:
        import capo_sagemaker.types.s3_data_source

        out["s3_data_source"] = (
            capo_sagemaker.types.s3_data_source.deserialize_aws_json_1_1(
                data["S3DataSource"]
            )
        )
    if "FileSystemDataSource" in data:
        import capo_sagemaker.types.file_system_data_source

        out["file_system_data_source"] = (
            capo_sagemaker.types.file_system_data_source.deserialize_aws_json_1_1(
                data["FileSystemDataSource"]
            )
        )
    if "DatasetSource" in data:
        import capo_sagemaker.types.dataset_source

        out["dataset_source"] = (
            capo_sagemaker.types.dataset_source.deserialize_aws_json_1_1(
                data["DatasetSource"]
            )
        )
    return out
