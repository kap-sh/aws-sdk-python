"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PromotionalMedia``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.promotional_embedded_image
    import capo_marketplace_discovery.types.promotional_embedded_video


class _PromotionalMedia_embeddedImage(TypedDict, closed=True):
    embeddedImage: "capo_marketplace_discovery.types.promotional_embedded_image.PromotionalEmbeddedImage"


class _PromotionalMedia_embeddedVideo(TypedDict, closed=True):
    embeddedVideo: "capo_marketplace_discovery.types.promotional_embedded_video.PromotionalEmbeddedVideo"


PromotionalMedia: TypeAlias = (
    _PromotionalMedia_embeddedImage | _PromotionalMedia_embeddedVideo
)


# --- restJson1 ser/de ---
def serialize_json(value: PromotionalMedia) -> dict:
    if "embeddedImage" in value:
        import capo_marketplace_discovery.types.promotional_embedded_image

        return {
            "embeddedImage": capo_marketplace_discovery.types.promotional_embedded_image.serialize_json(
                value["embeddedImage"]
            )
        }
    elif "embeddedVideo" in value:
        import capo_marketplace_discovery.types.promotional_embedded_video

        return {
            "embeddedVideo": capo_marketplace_discovery.types.promotional_embedded_video.serialize_json(
                value["embeddedVideo"]
            )
        }
    else:
        raise SerializationError("PromotionalMedia: no variant present")


def deserialize_json(data: dict) -> PromotionalMedia:
    if "embeddedImage" in data:
        import capo_marketplace_discovery.types.promotional_embedded_image

        return {
            "embeddedImage": capo_marketplace_discovery.types.promotional_embedded_image.deserialize_json(
                data["embeddedImage"]
            )
        }
    elif "embeddedVideo" in data:
        import capo_marketplace_discovery.types.promotional_embedded_video

        return {
            "embeddedVideo": capo_marketplace_discovery.types.promotional_embedded_video.deserialize_json(
                data["embeddedVideo"]
            )
        }
    else:
        raise DeserializationError("PromotionalMedia: no recognized variant key")
