"""Generated from Smithy shape ``com.amazonaws.directoryservice#EventTopic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.created_date_time
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.topic_arn
    import aws_sdk_directory_service.types.topic_name
    import aws_sdk_directory_service.types.topic_status


class EventTopic(TypedDict, closed=True):
    directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>The Directory ID of an Directory Service directory that will publish status messages to an Amazon SNS topic.</p>"""
    topic_name: NotRequired["aws_sdk_directory_service.types.topic_name.TopicName"]
    """<p>The name of an Amazon SNS topic the receives status messages from the directory.</p>"""
    topic_arn: NotRequired["aws_sdk_directory_service.types.topic_arn.TopicArn"]
    """<p>The Amazon SNS topic ARN (Amazon Resource Name).</p>"""
    created_date_time: NotRequired[
        "aws_sdk_directory_service.types.created_date_time.CreatedDateTime"
    ]
    """<p>The date and time of when you associated your directory with the Amazon SNS topic.</p>"""
    status: NotRequired["aws_sdk_directory_service.types.topic_status.TopicStatus"]
    """<p>The topic registration status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTopic) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "created_date_time" in value:
        import aws_sdk_directory_service.types.created_date_time

        out["CreatedDateTime"] = (
            aws_sdk_directory_service.types.created_date_time.serialize_aws_json_1_1(
                value["created_date_time"]
            )
        )
    if "status" in value:
        import aws_sdk_directory_service.types.topic_status

        out["Status"] = (
            aws_sdk_directory_service.types.topic_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventTopic:
    out: EventTopic = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    if "CreatedDateTime" in data:
        import aws_sdk_directory_service.types.created_date_time

        out["created_date_time"] = (
            aws_sdk_directory_service.types.created_date_time.deserialize_aws_json_1_1(
                data["CreatedDateTime"]
            )
        )
    if "Status" in data:
        import aws_sdk_directory_service.types.topic_status

        out["status"] = (
            aws_sdk_directory_service.types.topic_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
