"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateDataRepositoryAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.data_repository_association_id
    import aws_sdk_fsx.types.megabytes
    import aws_sdk_fsx.types.s3_data_repository_configuration


class UpdateDataRepositoryAssociationRequest(TypedDict):
    association_id: NotRequired[
        "aws_sdk_fsx.types.data_repository_association_id.DataRepositoryAssociationId"
    ]
    """<p>The ID of the data repository association that you are updating.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    imported_file_chunk_size: NotRequired["aws_sdk_fsx.types.megabytes.Megabytes"]
    """<p>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.</p> <p>The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</p>"""
    s3: NotRequired[
        "aws_sdk_fsx.types.s3_data_repository_configuration.S3DataRepositoryConfiguration"
    ]
    """<p>The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataRepositoryAssociationRequest) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "imported_file_chunk_size" in value:
        out["ImportedFileChunkSize"] = value["imported_file_chunk_size"]
    if "s3" in value:
        import aws_sdk_fsx.types.s3_data_repository_configuration

        out["S3"] = (
            aws_sdk_fsx.types.s3_data_repository_configuration.serialize_aws_json_1_1(
                value["s3"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataRepositoryAssociationRequest:
    out: UpdateDataRepositoryAssociationRequest = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "ImportedFileChunkSize" in data:
        out["imported_file_chunk_size"] = data["ImportedFileChunkSize"]
    if "S3" in data:
        import aws_sdk_fsx.types.s3_data_repository_configuration

        out["s3"] = (
            aws_sdk_fsx.types.s3_data_repository_configuration.deserialize_aws_json_1_1(
                data["S3"]
            )
        )
    return out
