"""Generated from Smithy shape ``com.amazonaws.ecrpublic#Layer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.layer_availability
    import aws_sdk_ecr_public.types.layer_digest
    import aws_sdk_ecr_public.types.layer_size_in_bytes
    import aws_sdk_ecr_public.types.media_type


class Layer(TypedDict):
    layer_digest: NotRequired["aws_sdk_ecr_public.types.layer_digest.LayerDigest"]
    """<p>The <code>sha256</code> digest of the image layer.</p>"""
    layer_availability: NotRequired[
        "aws_sdk_ecr_public.types.layer_availability.LayerAvailability"
    ]
    """<p>The availability status of the image layer.</p>"""
    layer_size: NotRequired[
        "aws_sdk_ecr_public.types.layer_size_in_bytes.LayerSizeInBytes"
    ]
    """<p>The size, in bytes, of the image layer.</p>"""
    media_type: NotRequired["aws_sdk_ecr_public.types.media_type.MediaType"]
    """<p>The media type of the layer, such as <code>application/vnd.docker.image.rootfs.diff.tar.gzip</code> or <code>application/vnd.oci.image.layer.v1.tar+gzip</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Layer) -> dict:
    out: dict = {}
    if "layer_digest" in value:
        out["layerDigest"] = value["layer_digest"]
    if "layer_availability" in value:
        import aws_sdk_ecr_public.types.layer_availability

        out["layerAvailability"] = (
            aws_sdk_ecr_public.types.layer_availability.serialize_aws_json_1_1(
                value["layer_availability"]
            )
        )
    if "layer_size" in value:
        out["layerSize"] = value["layer_size"]
    if "media_type" in value:
        out["mediaType"] = value["media_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Layer:
    out: Layer = {}  # type: ignore[typeddict-item]
    if "layerDigest" in data:
        out["layer_digest"] = data["layerDigest"]
    if "layerAvailability" in data:
        import aws_sdk_ecr_public.types.layer_availability

        out["layer_availability"] = (
            aws_sdk_ecr_public.types.layer_availability.deserialize_aws_json_1_1(
                data["layerAvailability"]
            )
        )
    if "layerSize" in data:
        out["layer_size"] = data["layerSize"]
    if "mediaType" in data:
        out["media_type"] = data["mediaType"]
    return out
