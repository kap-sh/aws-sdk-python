"""Generated from Smithy shape ``com.amazonaws.ecr#UploadLayerPartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.layer_part_blob
    import aws_sdk_ecr.types.part_size
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.upload_id


class UploadLayerPartRequest(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository to which you are uploading layer parts.</p>"""
    upload_id: "aws_sdk_ecr.types.upload_id.UploadId"
    """<p>The upload ID from a previous <a>InitiateLayerUpload</a> operation to associate with the layer part upload.</p>"""
    part_first_byte: "aws_sdk_ecr.types.part_size.PartSize"
    """<p>The position of the first byte of the layer part witin the overall image layer.</p>"""
    part_last_byte: "aws_sdk_ecr.types.part_size.PartSize"
    """<p>The position of the last byte of the layer part within the overall image layer.</p>"""
    layer_part_blob: "aws_sdk_ecr.types.layer_part_blob.LayerPartBlob"
    """<p>The base64-encoded layer part payload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadLayerPartRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["uploadId"] = value["upload_id"]
    out["partFirstByte"] = value["part_first_byte"]
    out["partLastByte"] = value["part_last_byte"]
    import aws_sdk_ecr.types.layer_part_blob

    out["layerPartBlob"] = aws_sdk_ecr.types.layer_part_blob.serialize_aws_json_1_1(
        value["layer_part_blob"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UploadLayerPartRequest:
    out: UploadLayerPartRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("UploadLayerPartRequest.repository_name required")
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("UploadLayerPartRequest.upload_id required")
    if "partFirstByte" in data:
        out["part_first_byte"] = data["partFirstByte"]
    else:
        raise DeserializationError("UploadLayerPartRequest.part_first_byte required")
    if "partLastByte" in data:
        out["part_last_byte"] = data["partLastByte"]
    else:
        raise DeserializationError("UploadLayerPartRequest.part_last_byte required")
    if "layerPartBlob" in data:
        import aws_sdk_ecr.types.layer_part_blob

        out["layer_part_blob"] = (
            aws_sdk_ecr.types.layer_part_blob.deserialize_aws_json_1_1(
                data["layerPartBlob"]
            )
        )
    else:
        raise DeserializationError("UploadLayerPartRequest.layer_part_blob required")
    return out
