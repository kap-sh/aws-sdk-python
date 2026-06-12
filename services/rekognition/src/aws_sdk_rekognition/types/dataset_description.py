"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_stats
    import aws_sdk_rekognition.types.dataset_status
    import aws_sdk_rekognition.types.dataset_status_message_code
    import aws_sdk_rekognition.types.date_time
    import aws_sdk_rekognition.types.status_message


class DatasetDescription(TypedDict):
    creation_timestamp: NotRequired["aws_sdk_rekognition.types.date_time.DateTime"]
    """<p> The Unix timestamp for the time and date that the dataset was created. </p>"""
    last_updated_timestamp: NotRequired["aws_sdk_rekognition.types.date_time.DateTime"]
    """<p> The Unix timestamp for the date and time that the dataset was last updated. </p>"""
    status: NotRequired["aws_sdk_rekognition.types.dataset_status.DatasetStatus"]
    """<p> The status of the dataset. </p>"""
    status_message: NotRequired[
        "aws_sdk_rekognition.types.status_message.StatusMessage"
    ]
    """<p> The status message for the dataset. </p>"""
    status_message_code: NotRequired[
        "aws_sdk_rekognition.types.dataset_status_message_code.DatasetStatusMessageCode"
    ]
    """<p> The status message code for the dataset operation. If a service error occurs, try the API call again later. If a client error occurs, check the input parameters to the dataset API call that failed. </p>"""
    dataset_stats: NotRequired["aws_sdk_rekognition.types.dataset_stats.DatasetStats"]
    """<p> The status message code for the dataset. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetDescription) -> dict:
    out: dict = {}
    if "creation_timestamp" in value:
        import aws_sdk_rekognition.types.date_time

        out["CreationTimestamp"] = (
            aws_sdk_rekognition.types.date_time.serialize_aws_json_1_1(
                value["creation_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_rekognition.types.date_time

        out["LastUpdatedTimestamp"] = (
            aws_sdk_rekognition.types.date_time.serialize_aws_json_1_1(
                value["last_updated_timestamp"]
            )
        )
    if "status" in value:
        import aws_sdk_rekognition.types.dataset_status

        out["Status"] = aws_sdk_rekognition.types.dataset_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "status_message_code" in value:
        import aws_sdk_rekognition.types.dataset_status_message_code

        out["StatusMessageCode"] = (
            aws_sdk_rekognition.types.dataset_status_message_code.serialize_aws_json_1_1(
                value["status_message_code"]
            )
        )
    if "dataset_stats" in value:
        import aws_sdk_rekognition.types.dataset_stats

        out["DatasetStats"] = (
            aws_sdk_rekognition.types.dataset_stats.serialize_aws_json_1_1(
                value["dataset_stats"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetDescription:
    out: DatasetDescription = {}  # type: ignore[typeddict-item]
    if "CreationTimestamp" in data:
        import aws_sdk_rekognition.types.date_time

        out["creation_timestamp"] = (
            aws_sdk_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_rekognition.types.date_time

        out["last_updated_timestamp"] = (
            aws_sdk_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["LastUpdatedTimestamp"]
            )
        )
    if "Status" in data:
        import aws_sdk_rekognition.types.dataset_status

        out["status"] = (
            aws_sdk_rekognition.types.dataset_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "StatusMessageCode" in data:
        import aws_sdk_rekognition.types.dataset_status_message_code

        out["status_message_code"] = (
            aws_sdk_rekognition.types.dataset_status_message_code.deserialize_aws_json_1_1(
                data["StatusMessageCode"]
            )
        )
    if "DatasetStats" in data:
        import aws_sdk_rekognition.types.dataset_stats

        out["dataset_stats"] = (
            aws_sdk_rekognition.types.dataset_stats.deserialize_aws_json_1_1(
                data["DatasetStats"]
            )
        )
    return out
