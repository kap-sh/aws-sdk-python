"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteDataRepositoryAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.data_repository_association_id
    import aws_sdk_fsx.types.delete_data_in_file_system


class DeleteDataRepositoryAssociationRequest(TypedDict):
    association_id: NotRequired[
        "aws_sdk_fsx.types.data_repository_association_id.DataRepositoryAssociationId"
    ]
    """<p>The ID of the data repository association that you want to delete.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    delete_data_in_file_system: NotRequired[
        "aws_sdk_fsx.types.delete_data_in_file_system.DeleteDataInFileSystem"
    ]
    """<p>Set to <code>true</code> to delete the data in the file system that corresponds to the data repository association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataRepositoryAssociationRequest) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "delete_data_in_file_system" in value:
        out["DeleteDataInFileSystem"] = value["delete_data_in_file_system"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataRepositoryAssociationRequest:
    out: DeleteDataRepositoryAssociationRequest = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "DeleteDataInFileSystem" in data:
        out["delete_data_in_file_system"] = data["DeleteDataInFileSystem"]
    return out
