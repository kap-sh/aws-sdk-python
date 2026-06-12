"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeEventTopicsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.topic_names


class DescribeEventTopicsRequest(TypedDict):
    directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>The Directory ID for which to get the list of associated Amazon SNS topics. If this member is null, associations for all Directory IDs are returned.</p>"""
    topic_names: NotRequired["aws_sdk_directory_service.types.topic_names.TopicNames"]
    """<p>A list of Amazon SNS topic names for which to obtain the information. If this member is null, all associations for the specified Directory ID are returned.</p> <p>An empty list results in an <code>InvalidParameterException</code> being thrown.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventTopicsRequest) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "topic_names" in value:
        import aws_sdk_directory_service.types.topic_names

        out["TopicNames"] = (
            aws_sdk_directory_service.types.topic_names.serialize_aws_json_1_1(
                value["topic_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventTopicsRequest:
    out: DescribeEventTopicsRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "TopicNames" in data:
        import aws_sdk_directory_service.types.topic_names

        out["topic_names"] = (
            aws_sdk_directory_service.types.topic_names.deserialize_aws_json_1_1(
                data["TopicNames"]
            )
        )
    return out
