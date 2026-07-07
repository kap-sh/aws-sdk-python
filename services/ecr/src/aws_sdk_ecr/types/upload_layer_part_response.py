"""Generated from Smithy shape ``com.amazonaws.ecr#UploadLayerPartResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.part_size
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.upload_id


class UploadLayerPartResponse(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    upload_id: NotRequired["aws_sdk_ecr.types.upload_id.UploadId"]
    """<p>The upload ID associated with the request.</p>"""
    last_byte_received: NotRequired["aws_sdk_ecr.types.part_size.PartSize"]
    """<p>The integer value of the last byte received in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadLayerPartResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "upload_id" in value:
        out["uploadId"] = value["upload_id"]
    if "last_byte_received" in value:
        out["lastByteReceived"] = value["last_byte_received"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UploadLayerPartResponse:
    out: UploadLayerPartResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    if "lastByteReceived" in data:
        out["last_byte_received"] = data["lastByteReceived"]
    return out
