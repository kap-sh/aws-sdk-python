"""Generated from Smithy shape ``com.amazonaws.fsx#ReleaseFileSystemNfsV3LocksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.file_system_id


class ReleaseFileSystemNfsV3LocksRequest(TypedDict, closed=True):
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseFileSystemNfsV3LocksRequest) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReleaseFileSystemNfsV3LocksRequest:
    out: ReleaseFileSystemNfsV3LocksRequest = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
