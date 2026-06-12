"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.any_length_string
    import aws_sdk_comprehend.types.comprehend_arn_name
    import aws_sdk_comprehend.types.comprehend_dataset_arn
    import aws_sdk_comprehend.types.dataset_status
    import aws_sdk_comprehend.types.dataset_type
    import aws_sdk_comprehend.types.description
    import aws_sdk_comprehend.types.number_of_documents
    import aws_sdk_comprehend.types.s3_uri
    import aws_sdk_comprehend.types.timestamp


class DatasetProperties(TypedDict):
    dataset_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_dataset_arn.ComprehendDatasetArn"
    ]
    """<p>The ARN of the dataset.</p>"""
    dataset_name: NotRequired[
        "aws_sdk_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p>The name of the dataset.</p>"""
    dataset_type: NotRequired["aws_sdk_comprehend.types.dataset_type.DatasetType"]
    """<p>The dataset type (training data or test data).</p>"""
    dataset_s3_uri: NotRequired["aws_sdk_comprehend.types.s3_uri.S3Uri"]
    """<p>The S3 URI where the dataset is stored.</p>"""
    description: NotRequired["aws_sdk_comprehend.types.description.Description"]
    """<p>Description of the dataset.</p>"""
    status: NotRequired["aws_sdk_comprehend.types.dataset_status.DatasetStatus"]
    """<p>The dataset status. While the system creates the dataset, the status is <code>CREATING</code>. When the dataset is ready to use, the status changes to <code>COMPLETED</code>. </p>"""
    message: NotRequired["aws_sdk_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of the dataset.</p>"""
    number_of_documents: NotRequired[
        "aws_sdk_comprehend.types.number_of_documents.NumberOfDocuments"
    ]
    """<p>The number of documents in the dataset.</p>"""
    creation_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Creation time of the dataset.</p>"""
    end_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Time when the data from the dataset becomes available in the data lake.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetProperties) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_type" in value:
        import aws_sdk_comprehend.types.dataset_type

        out["DatasetType"] = (
            aws_sdk_comprehend.types.dataset_type.serialize_aws_json_1_1(
                value["dataset_type"]
            )
        )
    if "dataset_s3_uri" in value:
        out["DatasetS3Uri"] = value["dataset_s3_uri"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_comprehend.types.dataset_status

        out["Status"] = aws_sdk_comprehend.types.dataset_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "number_of_documents" in value:
        out["NumberOfDocuments"] = value["number_of_documents"]
    if "creation_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["EndTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetProperties:
    out: DatasetProperties = {}  # type: ignore[typeddict-item]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "DatasetType" in data:
        import aws_sdk_comprehend.types.dataset_type

        out["dataset_type"] = (
            aws_sdk_comprehend.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    if "DatasetS3Uri" in data:
        out["dataset_s3_uri"] = data["DatasetS3Uri"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_comprehend.types.dataset_status

        out["status"] = (
            aws_sdk_comprehend.types.dataset_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "NumberOfDocuments" in data:
        out["number_of_documents"] = data["NumberOfDocuments"]
    if "CreationTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["end_time"] = aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
