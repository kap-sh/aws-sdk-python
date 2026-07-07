"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateLogSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.log_group_name


class CreateLogSubscriptionRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the directory to which you want to subscribe and receive real-time logs to your specified CloudWatch log group.</p>"""
    log_group_name: "aws_sdk_directory_service.types.log_group_name.LogGroupName"
    """<p>The name of the CloudWatch log group where the real-time domain controller logs are forwarded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLogSubscriptionRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["LogGroupName"] = value["log_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLogSubscriptionRequest:
    out: CreateLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("CreateLogSubscriptionRequest.directory_id required")
    if "LogGroupName" in data:
        out["log_group_name"] = data["LogGroupName"]
    else:
        raise DeserializationError(
            "CreateLogSubscriptionRequest.log_group_name required"
        )
    return out
