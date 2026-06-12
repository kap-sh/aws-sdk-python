"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableRadiusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id


class DisableRadiusRequest(TypedDict):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to disable MFA.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableRadiusRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableRadiusRequest:
    out: DisableRadiusRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("DisableRadiusRequest.directory_id required")
    return out
