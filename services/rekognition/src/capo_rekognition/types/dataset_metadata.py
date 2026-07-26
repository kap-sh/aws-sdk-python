"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_arn
    import capo_rekognition.types.dataset_status
    import capo_rekognition.types.dataset_status_message_code
    import capo_rekognition.types.dataset_type
    import capo_rekognition.types.date_time
    import capo_rekognition.types.status_message


class DatasetMetadata(TypedDict, closed=True):
    creation_timestamp: NotRequired["capo_rekognition.types.date_time.DateTime"]
    """<p> The Unix timestamp for the date and time that the dataset was created. </p>"""
    dataset_type: NotRequired["capo_rekognition.types.dataset_type.DatasetType"]
    """<p> The type of the dataset. </p>"""
    dataset_arn: NotRequired["capo_rekognition.types.dataset_arn.DatasetArn"]
    """<p> The Amazon Resource Name (ARN) for the dataset. </p>"""
    status: NotRequired["capo_rekognition.types.dataset_status.DatasetStatus"]
    """<p> The status for the dataset. </p>"""
    status_message: NotRequired["capo_rekognition.types.status_message.StatusMessage"]
    """<p> The status message for the dataset. </p>"""
    status_message_code: NotRequired[
        "capo_rekognition.types.dataset_status_message_code.DatasetStatusMessageCode"
    ]
    """<p> The status message code for the dataset operation. If a service error occurs, try the API call again later. If a client error occurs, check the input parameters to the dataset API call that failed. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetMetadata) -> dict:
    out: dict = {}
    if "creation_timestamp" in value:
        import capo_rekognition.types.date_time

        out["CreationTimestamp"] = (
            capo_rekognition.types.date_time.serialize_aws_json_1_1(
                value["creation_timestamp"]
            )
        )
    if "dataset_type" in value:
        import capo_rekognition.types.dataset_type

        out["DatasetType"] = capo_rekognition.types.dataset_type.serialize_aws_json_1_1(
            value["dataset_type"]
        )
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "status" in value:
        import capo_rekognition.types.dataset_status

        out["Status"] = capo_rekognition.types.dataset_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "status_message_code" in value:
        import capo_rekognition.types.dataset_status_message_code

        out["StatusMessageCode"] = (
            capo_rekognition.types.dataset_status_message_code.serialize_aws_json_1_1(
                value["status_message_code"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetMetadata:
    out: DatasetMetadata = {}  # type: ignore[typeddict-item]
    if "CreationTimestamp" in data:
        import capo_rekognition.types.date_time

        out["creation_timestamp"] = (
            capo_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    if "DatasetType" in data:
        import capo_rekognition.types.dataset_type

        out["dataset_type"] = (
            capo_rekognition.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "Status" in data:
        import capo_rekognition.types.dataset_status

        out["status"] = capo_rekognition.types.dataset_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "StatusMessageCode" in data:
        import capo_rekognition.types.dataset_status_message_code

        out["status_message_code"] = (
            capo_rekognition.types.dataset_status_message_code.deserialize_aws_json_1_1(
                data["StatusMessageCode"]
            )
        )
    return out
