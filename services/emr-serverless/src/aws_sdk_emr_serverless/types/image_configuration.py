"""Generated from Smithy shape ``com.amazonaws.emrserverless#ImageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.image_digest
    import aws_sdk_emr_serverless.types.image_uri


class ImageConfiguration(TypedDict):
    image_uri: "aws_sdk_emr_serverless.types.image_uri.ImageUri"
    """<p>The image URI.</p>"""
    resolved_image_digest: NotRequired[
        "aws_sdk_emr_serverless.types.image_digest.ImageDigest"
    ]
    """<p>The SHA256 digest of the image URI. This indicates which specific image the application is configured for. The image digest doesn't exist until an application has started.</p>"""
    application_level_digest_resolution: NotRequired["bool"]
    """<p>Boolean value indicating if the digest resolution is application level or workload level. If true, a custom image URI is resolved at application start time and all workloads submitted will use that image digest. If false, the custom image URI is resolved at the workload submission time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfiguration) -> dict:
    out: dict = {}
    out["imageUri"] = value["image_uri"]
    if "resolved_image_digest" in value:
        out["resolvedImageDigest"] = value["resolved_image_digest"]
    if "application_level_digest_resolution" in value:
        out["applicationLevelDigestResolution"] = value[
            "application_level_digest_resolution"
        ]
    return out


def deserialize_json(data: dict) -> ImageConfiguration:
    out: ImageConfiguration = {}  # type: ignore[typeddict-item]
    if "imageUri" in data:
        out["image_uri"] = data["imageUri"]
    else:
        raise DeserializationError("ImageConfiguration.image_uri required")
    if "resolvedImageDigest" in data:
        out["resolved_image_digest"] = data["resolvedImageDigest"]
    if "applicationLevelDigestResolution" in data:
        out["application_level_digest_resolution"] = data[
            "applicationLevelDigestResolution"
        ]
    return out
