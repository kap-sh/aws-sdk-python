"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_configuration_status
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.next_token


class DescribeSettingsRequest(TypedDict):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to retrieve information.</p>"""
    status: NotRequired[
        "aws_sdk_directory_service.types.directory_configuration_status.DirectoryConfigurationStatus"
    ]
    """<p>The status of the directory settings for which to retrieve information.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>The <code>DescribeSettingsResult.NextToken</code> value from a previous call to <a>DescribeSettings</a>. Pass null if this is the first call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSettingsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "status" in value:
        import aws_sdk_directory_service.types.directory_configuration_status

        out["Status"] = (
            aws_sdk_directory_service.types.directory_configuration_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSettingsRequest:
    out: DescribeSettingsRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("DescribeSettingsRequest.directory_id required")
    if "Status" in data:
        import aws_sdk_directory_service.types.directory_configuration_status

        out["status"] = (
            aws_sdk_directory_service.types.directory_configuration_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
