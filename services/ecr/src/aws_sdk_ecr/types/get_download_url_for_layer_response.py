"""Generated from Smithy shape ``com.amazonaws.ecr#GetDownloadUrlForLayerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.layer_digest
    import aws_sdk_ecr.types.url


class GetDownloadUrlForLayerResponse(TypedDict, closed=True):
    download_url: NotRequired["aws_sdk_ecr.types.url.Url"]
    """<p>The pre-signed Amazon S3 download URL for the requested layer.</p>"""
    layer_digest: NotRequired["aws_sdk_ecr.types.layer_digest.LayerDigest"]
    """<p>The digest of the image layer to download.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDownloadUrlForLayerResponse) -> dict:
    out: dict = {}
    if "download_url" in value:
        out["downloadUrl"] = value["download_url"]
    if "layer_digest" in value:
        out["layerDigest"] = value["layer_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDownloadUrlForLayerResponse:
    out: GetDownloadUrlForLayerResponse = {}  # type: ignore[typeddict-item]
    if "downloadUrl" in data:
        out["download_url"] = data["downloadUrl"]
    if "layerDigest" in data:
        out["layer_digest"] = data["layerDigest"]
    return out
