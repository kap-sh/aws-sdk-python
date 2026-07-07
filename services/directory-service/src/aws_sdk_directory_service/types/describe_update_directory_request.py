"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeUpdateDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.next_token
    import aws_sdk_directory_service.types.region_name
    import aws_sdk_directory_service.types.update_type


class DescribeUpdateDirectoryRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p> The unique identifier of the directory. </p>"""
    update_type: "aws_sdk_directory_service.types.update_type.UpdateType"
    """<p> The type of updates you want to describe for the directory. </p>"""
    region_name: NotRequired["aws_sdk_directory_service.types.region_name.RegionName"]
    """<p> The name of the Region. </p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p> The <code>DescribeUpdateDirectoryResult</code>. NextToken value from a previous call to <a>DescribeUpdateDirectory</a>. Pass null if this is the first call. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUpdateDirectoryRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import aws_sdk_directory_service.types.update_type

    out["UpdateType"] = (
        aws_sdk_directory_service.types.update_type.serialize_aws_json_1_1(
            value["update_type"]
        )
    )
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUpdateDirectoryRequest:
    out: DescribeUpdateDirectoryRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError(
            "DescribeUpdateDirectoryRequest.directory_id required"
        )
    if "UpdateType" in data:
        import aws_sdk_directory_service.types.update_type

        out["update_type"] = (
            aws_sdk_directory_service.types.update_type.deserialize_aws_json_1_1(
                data["UpdateType"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeUpdateDirectoryRequest.update_type required"
        )
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
