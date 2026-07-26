"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.transport_media_info


class _RouterInputMetadata_TransportStreamMediaInfo(TypedDict, closed=True):
    TransportStreamMediaInfo: (
        "capo_mediaconnect.types.transport_media_info.TransportMediaInfo"
    )


RouterInputMetadata: TypeAlias = _RouterInputMetadata_TransportStreamMediaInfo


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputMetadata) -> dict:
    if "TransportStreamMediaInfo" in value:
        import capo_mediaconnect.types.transport_media_info

        return {
            "transportStreamMediaInfo": capo_mediaconnect.types.transport_media_info.serialize_json(
                value["TransportStreamMediaInfo"]
            )
        }
    else:
        raise SerializationError("RouterInputMetadata: no variant present")


def deserialize_json(data: dict) -> RouterInputMetadata:
    if "transportStreamMediaInfo" in data:
        import capo_mediaconnect.types.transport_media_info

        return {
            "TransportStreamMediaInfo": capo_mediaconnect.types.transport_media_info.deserialize_json(
                data["transportStreamMediaInfo"]
            )
        }
    else:
        raise DeserializationError("RouterInputMetadata: no recognized variant key")
