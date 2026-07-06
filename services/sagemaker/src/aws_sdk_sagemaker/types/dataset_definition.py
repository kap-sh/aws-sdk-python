"""Generated from Smithy shape ``com.amazonaws.sagemaker#DatasetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.athena_dataset_definition
    import aws_sdk_sagemaker.types.data_distribution_type
    import aws_sdk_sagemaker.types.input_mode
    import aws_sdk_sagemaker.types.processing_local_path
    import aws_sdk_sagemaker.types.redshift_dataset_definition


class DatasetDefinition(TypedDict, closed=True):
    athena_dataset_definition: NotRequired[
        "aws_sdk_sagemaker.types.athena_dataset_definition.AthenaDatasetDefinition"
    ]
    redshift_dataset_definition: NotRequired[
        "aws_sdk_sagemaker.types.redshift_dataset_definition.RedshiftDatasetDefinition"
    ]
    local_path: NotRequired[
        "aws_sdk_sagemaker.types.processing_local_path.ProcessingLocalPath"
    ]
    """<p>The local path where you want Amazon SageMaker to download the Dataset Definition inputs to run a processing job. <code>LocalPath</code> is an absolute path to the input data. This is a required parameter when <code>AppManaged</code> is <code>False</code> (default).</p>"""
    data_distribution_type: NotRequired[
        "aws_sdk_sagemaker.types.data_distribution_type.DataDistributionType"
    ]
    """<p>Whether the generated dataset is <code>FullyReplicated</code> or <code>ShardedByS3Key</code> (default).</p>"""
    input_mode: NotRequired["aws_sdk_sagemaker.types.input_mode.InputMode"]
    """<p>Whether to use <code>File</code> or <code>Pipe</code> input mode. In <code>File</code> (default) mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode. In <code>Pipe</code> mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetDefinition) -> dict:
    out: dict = {}
    if "athena_dataset_definition" in value:
        import aws_sdk_sagemaker.types.athena_dataset_definition

        out["AthenaDatasetDefinition"] = (
            aws_sdk_sagemaker.types.athena_dataset_definition.serialize_aws_json_1_1(
                value["athena_dataset_definition"]
            )
        )
    if "redshift_dataset_definition" in value:
        import aws_sdk_sagemaker.types.redshift_dataset_definition

        out["RedshiftDatasetDefinition"] = (
            aws_sdk_sagemaker.types.redshift_dataset_definition.serialize_aws_json_1_1(
                value["redshift_dataset_definition"]
            )
        )
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "data_distribution_type" in value:
        import aws_sdk_sagemaker.types.data_distribution_type

        out["DataDistributionType"] = (
            aws_sdk_sagemaker.types.data_distribution_type.serialize_aws_json_1_1(
                value["data_distribution_type"]
            )
        )
    if "input_mode" in value:
        import aws_sdk_sagemaker.types.input_mode

        out["InputMode"] = aws_sdk_sagemaker.types.input_mode.serialize_aws_json_1_1(
            value["input_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetDefinition:
    out: DatasetDefinition = {}  # type: ignore[typeddict-item]
    if "AthenaDatasetDefinition" in data:
        import aws_sdk_sagemaker.types.athena_dataset_definition

        out["athena_dataset_definition"] = (
            aws_sdk_sagemaker.types.athena_dataset_definition.deserialize_aws_json_1_1(
                data["AthenaDatasetDefinition"]
            )
        )
    if "RedshiftDatasetDefinition" in data:
        import aws_sdk_sagemaker.types.redshift_dataset_definition

        out["redshift_dataset_definition"] = (
            aws_sdk_sagemaker.types.redshift_dataset_definition.deserialize_aws_json_1_1(
                data["RedshiftDatasetDefinition"]
            )
        )
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    if "DataDistributionType" in data:
        import aws_sdk_sagemaker.types.data_distribution_type

        out["data_distribution_type"] = (
            aws_sdk_sagemaker.types.data_distribution_type.deserialize_aws_json_1_1(
                data["DataDistributionType"]
            )
        )
    if "InputMode" in data:
        import aws_sdk_sagemaker.types.input_mode

        out["input_mode"] = aws_sdk_sagemaker.types.input_mode.deserialize_aws_json_1_1(
            data["InputMode"]
        )
    return out
