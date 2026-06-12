"""Generated from Smithy shape ``com.amazonaws.directoryservice#AcceptSharedDirectoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id


class AcceptSharedDirectoryRequest(TypedDict):
    shared_directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptSharedDirectoryRequest) -> dict:
    out: dict = {}
    out["SharedDirectoryId"] = value["shared_directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptSharedDirectoryRequest:
    out: AcceptSharedDirectoryRequest = {}  # type: ignore[typeddict-item]
    if "SharedDirectoryId" in data:
        out["shared_directory_id"] = data["SharedDirectoryId"]
    else:
        raise DeserializationError(
            "AcceptSharedDirectoryRequest.shared_directory_id required"
        )
    return out
