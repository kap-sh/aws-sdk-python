"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyEndpointEncryptionModeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.endpoint_encryption_mode


class ModifyEndpointEncryptionModeRequest(TypedDict):
    directory_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p> The identifier of the directory.</p>"""
    endpoint_encryption_mode: (
        "aws_sdk_workspaces.types.endpoint_encryption_mode.EndpointEncryptionMode"
    )
    """<p>The encryption mode used for endpoint connections when streaming to WorkSpaces Personal or WorkSpace Pools.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyEndpointEncryptionModeRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import aws_sdk_workspaces.types.endpoint_encryption_mode

    out["EndpointEncryptionMode"] = (
        aws_sdk_workspaces.types.endpoint_encryption_mode.serialize_aws_json_1_1(
            value["endpoint_encryption_mode"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyEndpointEncryptionModeRequest:
    out: ModifyEndpointEncryptionModeRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError(
            "ModifyEndpointEncryptionModeRequest.directory_id required"
        )
    if "EndpointEncryptionMode" in data:
        import aws_sdk_workspaces.types.endpoint_encryption_mode

        out["endpoint_encryption_mode"] = (
            aws_sdk_workspaces.types.endpoint_encryption_mode.deserialize_aws_json_1_1(
                data["EndpointEncryptionMode"]
            )
        )
    else:
        raise DeserializationError(
            "ModifyEndpointEncryptionModeRequest.endpoint_encryption_mode required"
        )
    return out
