"""Generated from Smithy shape ``com.amazonaws.ecr#ImageReferrer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.annotations
    import aws_sdk_ecr.types.artifact_status
    import aws_sdk_ecr.types.artifact_type
    import aws_sdk_ecr.types.image_digest
    import aws_sdk_ecr.types.image_size_in_bytes
    import aws_sdk_ecr.types.media_type


class ImageReferrer(TypedDict, closed=True):
    digest: "aws_sdk_ecr.types.image_digest.ImageDigest"
    """<p>The digest of the artifact manifest.</p>"""
    media_type: "aws_sdk_ecr.types.media_type.MediaType"
    """<p>The media type of the artifact manifest.</p>"""
    artifact_type: NotRequired["aws_sdk_ecr.types.artifact_type.ArtifactType"]
    """<p>A string identifying the type of artifact.</p>"""
    size: "aws_sdk_ecr.types.image_size_in_bytes.ImageSizeInBytes"
    """<p>The size, in bytes, of the artifact.</p>"""
    annotations: NotRequired["aws_sdk_ecr.types.annotations.Annotations"]
    """<p>A map of annotations associated with the artifact.</p>"""
    artifact_status: NotRequired["aws_sdk_ecr.types.artifact_status.ArtifactStatus"]
    """<p>The status of the artifact. Valid values are <code>ACTIVE</code>, <code>ARCHIVED</code>, or <code>ACTIVATING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageReferrer) -> dict:
    out: dict = {}
    out["digest"] = value["digest"]
    out["mediaType"] = value["media_type"]
    if "artifact_type" in value:
        out["artifactType"] = value["artifact_type"]
    out["size"] = value["size"]
    if "annotations" in value:
        import aws_sdk_ecr.types.annotations

        out["annotations"] = aws_sdk_ecr.types.annotations.serialize_aws_json_1_1(
            value["annotations"]
        )
    if "artifact_status" in value:
        import aws_sdk_ecr.types.artifact_status

        out["artifactStatus"] = (
            aws_sdk_ecr.types.artifact_status.serialize_aws_json_1_1(
                value["artifact_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageReferrer:
    out: ImageReferrer = {}  # type: ignore[typeddict-item]
    if "digest" in data:
        out["digest"] = data["digest"]
    else:
        raise DeserializationError("ImageReferrer.digest required")
    if "mediaType" in data:
        out["media_type"] = data["mediaType"]
    else:
        raise DeserializationError("ImageReferrer.media_type required")
    if "artifactType" in data:
        out["artifact_type"] = data["artifactType"]
    if "size" in data:
        out["size"] = data["size"]
    else:
        raise DeserializationError("ImageReferrer.size required")
    if "annotations" in data:
        import aws_sdk_ecr.types.annotations

        out["annotations"] = aws_sdk_ecr.types.annotations.deserialize_aws_json_1_1(
            data["annotations"]
        )
    if "artifactStatus" in data:
        import aws_sdk_ecr.types.artifact_status

        out["artifact_status"] = (
            aws_sdk_ecr.types.artifact_status.deserialize_aws_json_1_1(
                data["artifactStatus"]
            )
        )
    return out
