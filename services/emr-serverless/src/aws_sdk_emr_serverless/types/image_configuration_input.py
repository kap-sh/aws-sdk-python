"""Generated from Smithy shape ``com.amazonaws.emrserverless#ImageConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.image_uri


class ImageConfigurationInput(TypedDict):
    image_uri: NotRequired["aws_sdk_emr_serverless.types.image_uri.ImageUri"]
    """<p>The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.</p>"""
    application_level_digest_resolution: NotRequired["bool"]
    """<p>Boolean value indicating if the digest resolution is application level or workload level. If true, a custom image URI is resolved at application start time and all workloads submitted will use that image digest. If false, the custom image URI is resolved at the workload submission time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfigurationInput) -> dict:
    out: dict = {}
    if "image_uri" in value:
        out["imageUri"] = value["image_uri"]
    if "application_level_digest_resolution" in value:
        out["applicationLevelDigestResolution"] = value[
            "application_level_digest_resolution"
        ]
    return out


def deserialize_json(data: dict) -> ImageConfigurationInput:
    out: ImageConfigurationInput = {}  # type: ignore[typeddict-item]
    if "imageUri" in data:
        out["image_uri"] = data["imageUri"]
    if "applicationLevelDigestResolution" in data:
        out["application_level_digest_resolution"] = data[
            "applicationLevelDigestResolution"
        ]
    return out
