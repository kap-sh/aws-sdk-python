"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteConditionalForwarderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.remote_domain_name


class DeleteConditionalForwarderRequest(TypedDict):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The directory ID for which you are deleting the conditional forwarder.</p>"""
    remote_domain_name: (
        "aws_sdk_directory_service.types.remote_domain_name.RemoteDomainName"
    )
    """<p>The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConditionalForwarderRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["RemoteDomainName"] = value["remote_domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConditionalForwarderRequest:
    out: DeleteConditionalForwarderRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError(
            "DeleteConditionalForwarderRequest.directory_id required"
        )
    if "RemoteDomainName" in data:
        out["remote_domain_name"] = data["RemoteDomainName"]
    else:
        raise DeserializationError(
            "DeleteConditionalForwarderRequest.remote_domain_name required"
        )
    return out
