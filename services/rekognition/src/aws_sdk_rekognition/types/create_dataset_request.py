"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_source
    import aws_sdk_rekognition.types.dataset_type
    import aws_sdk_rekognition.types.project_arn
    import aws_sdk_rekognition.types.tag_map


class CreateDatasetRequest(TypedDict):
    dataset_source: NotRequired[
        "aws_sdk_rekognition.types.dataset_source.DatasetSource"
    ]
    """<p> The source files for the dataset. You can specify the ARN of an existing dataset or specify the Amazon S3 bucket location of an Amazon Sagemaker format manifest file. If you don't specify <code>datasetSource</code>, an empty dataset is created. To add labeled images to the dataset, You can use the console or call <a>UpdateDatasetEntries</a>. </p>"""
    dataset_type: "aws_sdk_rekognition.types.dataset_type.DatasetType"
    """<p> The type of the dataset. Specify <code>TRAIN</code> to create a training dataset. Specify <code>TEST</code> to create a test dataset. </p>"""
    project_arn: "aws_sdk_rekognition.types.project_arn.ProjectArn"
    """<p> The ARN of the Amazon Rekognition Custom Labels project to which you want to asssign the dataset. </p>"""
    tags: NotRequired["aws_sdk_rekognition.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that you want to attach to the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    if "dataset_source" in value:
        import aws_sdk_rekognition.types.dataset_source

        out["DatasetSource"] = (
            aws_sdk_rekognition.types.dataset_source.serialize_aws_json_1_1(
                value["dataset_source"]
            )
        )
    import aws_sdk_rekognition.types.dataset_type

    out["DatasetType"] = aws_sdk_rekognition.types.dataset_type.serialize_aws_json_1_1(
        value["dataset_type"]
    )
    out["ProjectArn"] = value["project_arn"]
    if "tags" in value:
        import aws_sdk_rekognition.types.tag_map

        out["Tags"] = aws_sdk_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "DatasetSource" in data:
        import aws_sdk_rekognition.types.dataset_source

        out["dataset_source"] = (
            aws_sdk_rekognition.types.dataset_source.deserialize_aws_json_1_1(
                data["DatasetSource"]
            )
        )
    if "DatasetType" in data:
        import aws_sdk_rekognition.types.dataset_type

        out["dataset_type"] = (
            aws_sdk_rekognition.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_type required")
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    else:
        raise DeserializationError("CreateDatasetRequest.project_arn required")
    if "Tags" in data:
        import aws_sdk_rekognition.types.tag_map

        out["tags"] = aws_sdk_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
