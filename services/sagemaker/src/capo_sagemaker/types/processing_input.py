"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_managed
    import capo_sagemaker.types.dataset_definition
    import capo_sagemaker.types.processing_s3_input
    import capo_sagemaker.types.string


class ProcessingInput(TypedDict, closed=True):
    input_name: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The name for the processing job input.</p>"""
    app_managed: NotRequired["capo_sagemaker.types.app_managed.AppManaged"]
    """<p>When <code>True</code>, input operations such as data download are managed natively by the processing job application. When <code>False</code> (default), input operations are managed by Amazon SageMaker.</p>"""
    s3_input: NotRequired["capo_sagemaker.types.processing_s3_input.ProcessingS3Input"]
    """<p>Configuration for downloading input data from Amazon S3 into the processing container.</p>"""
    dataset_definition: NotRequired[
        "capo_sagemaker.types.dataset_definition.DatasetDefinition"
    ]
    """<p>Configuration for a Dataset Definition input. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingInput) -> dict:
    out: dict = {}
    if "input_name" in value:
        out["InputName"] = value["input_name"]
    if "app_managed" in value:
        out["AppManaged"] = value["app_managed"]
    if "s3_input" in value:
        import capo_sagemaker.types.processing_s3_input

        out["S3Input"] = (
            capo_sagemaker.types.processing_s3_input.serialize_aws_json_1_1(
                value["s3_input"]
            )
        )
    if "dataset_definition" in value:
        import capo_sagemaker.types.dataset_definition

        out["DatasetDefinition"] = (
            capo_sagemaker.types.dataset_definition.serialize_aws_json_1_1(
                value["dataset_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingInput:
    out: ProcessingInput = {}  # type: ignore[typeddict-item]
    if "InputName" in data:
        out["input_name"] = data["InputName"]
    if "AppManaged" in data:
        out["app_managed"] = data["AppManaged"]
    if "S3Input" in data:
        import capo_sagemaker.types.processing_s3_input

        out["s3_input"] = (
            capo_sagemaker.types.processing_s3_input.deserialize_aws_json_1_1(
                data["S3Input"]
            )
        )
    if "DatasetDefinition" in data:
        import capo_sagemaker.types.dataset_definition

        out["dataset_definition"] = (
            capo_sagemaker.types.dataset_definition.deserialize_aws_json_1_1(
                data["DatasetDefinition"]
            )
        )
    return out
