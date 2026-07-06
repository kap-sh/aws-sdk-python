"""Generated from Smithy shape ``com.amazonaws.ecr#CompleteLayerUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.layer_digest_list
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.upload_id


class CompleteLayerUploadRequest(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository to associate with the image layer.</p>"""
    upload_id: "aws_sdk_ecr.types.upload_id.UploadId"
    """<p>The upload ID from a previous <a>InitiateLayerUpload</a> operation to associate with the image layer.</p>"""
    layer_digests: "aws_sdk_ecr.types.layer_digest_list.LayerDigestList"
    """<p>The <code>sha256</code> digest of the image layer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompleteLayerUploadRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["uploadId"] = value["upload_id"]
    import aws_sdk_ecr.types.layer_digest_list

    out["layerDigests"] = aws_sdk_ecr.types.layer_digest_list.serialize_aws_json_1_1(
        value["layer_digests"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompleteLayerUploadRequest:
    out: CompleteLayerUploadRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "CompleteLayerUploadRequest.repository_name required"
        )
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("CompleteLayerUploadRequest.upload_id required")
    if "layerDigests" in data:
        import aws_sdk_ecr.types.layer_digest_list

        out["layer_digests"] = (
            aws_sdk_ecr.types.layer_digest_list.deserialize_aws_json_1_1(
                data["layerDigests"]
            )
        )
    else:
        raise DeserializationError("CompleteLayerUploadRequest.layer_digests required")
    return out
