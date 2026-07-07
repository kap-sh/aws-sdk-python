"""Generated from Smithy shape ``com.amazonaws.fsx#StartMisconfiguredStateRecoveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.file_system_id


class StartMisconfiguredStateRecoveryRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMisconfiguredStateRecoveryRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMisconfiguredStateRecoveryRequest:
    out: StartMisconfiguredStateRecoveryRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    return out
