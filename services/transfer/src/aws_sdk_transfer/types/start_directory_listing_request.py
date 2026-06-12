"""Generated from Smithy shape ``com.amazonaws.transfer#StartDirectoryListingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.connector_id
    import aws_sdk_transfer.types.file_path
    import aws_sdk_transfer.types.max_items


class StartDirectoryListingRequest(TypedDict):
    connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId"
    """<p>The unique identifier for the connector.</p>"""
    remote_directory_path: "aws_sdk_transfer.types.file_path.FilePath"
    """<p>Specifies the directory on the remote SFTP server for which you want to list its contents.</p>"""
    max_items: NotRequired["aws_sdk_transfer.types.max_items.MaxItems"]
    """<p>An optional parameter where you can specify the maximum number of file/directory names to retrieve. The default value is 1,000.</p>"""
    output_directory_path: "aws_sdk_transfer.types.file_path.FilePath"
    """<p>Specifies the path (bucket and prefix) in Amazon S3 storage to store the results of the directory listing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDirectoryListingRequest) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    out["RemoteDirectoryPath"] = value["remote_directory_path"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    out["OutputDirectoryPath"] = value["output_directory_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDirectoryListingRequest:
    out: StartDirectoryListingRequest = {}  # type: ignore[typeddict-item]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    else:
        raise DeserializationError("StartDirectoryListingRequest.connector_id required")
    if "RemoteDirectoryPath" in data:
        out["remote_directory_path"] = data["RemoteDirectoryPath"]
    else:
        raise DeserializationError(
            "StartDirectoryListingRequest.remote_directory_path required"
        )
    if "MaxItems" in data:
        out["max_items"] = data["MaxItems"]
    if "OutputDirectoryPath" in data:
        out["output_directory_path"] = data["OutputDirectoryPath"]
    else:
        raise DeserializationError(
            "StartDirectoryListingRequest.output_directory_path required"
        )
    return out
