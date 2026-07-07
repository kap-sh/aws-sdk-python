"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteDataRepositoryAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_association_id
    import aws_sdk_fsx.types.data_repository_lifecycle
    import aws_sdk_fsx.types.delete_data_in_file_system


class DeleteDataRepositoryAssociationResponse(TypedDict, closed=True):
    association_id: NotRequired[
        "aws_sdk_fsx.types.data_repository_association_id.DataRepositoryAssociationId"
    ]
    """<p>The ID of the data repository association being deleted.</p>"""
    lifecycle: NotRequired[
        "aws_sdk_fsx.types.data_repository_lifecycle.DataRepositoryLifecycle"
    ]
    """<p>Describes the lifecycle state of the data repository association being deleted.</p>"""
    delete_data_in_file_system: NotRequired[
        "aws_sdk_fsx.types.delete_data_in_file_system.DeleteDataInFileSystem"
    ]
    """<p>Indicates whether data in the file system that corresponds to the data repository association is being deleted. Default is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataRepositoryAssociationResponse) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.data_repository_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.data_repository_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "delete_data_in_file_system" in value:
        out["DeleteDataInFileSystem"] = value["delete_data_in_file_system"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataRepositoryAssociationResponse:
    out: DeleteDataRepositoryAssociationResponse = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.data_repository_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.data_repository_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "DeleteDataInFileSystem" in data:
        out["delete_data_in_file_system"] = data["DeleteDataInFileSystem"]
    return out
