"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiSourceMetadataInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_message_detail
    import capo_mediaconnect.types.__list_of_ndi_source_info
    import capo_mediaconnect.types.ndi_media_info
    import capo_mediaconnect.types.ndi_source_info


class NdiSourceMetadataInfo(TypedDict, closed=True):
    active_source: NotRequired["capo_mediaconnect.types.ndi_source_info.NdiSourceInfo"]
    """<p> The connected NDI sender that's currently sending source content to the flow's NDI source. </p>"""
    discovered_sources: NotRequired[
        "capo_mediaconnect.types.__list_of_ndi_source_info.__listOfNdiSourceInfo"
    ]
    """<p> A list of the available upstream NDI senders aggregated from all of your configured discovery servers. </p>"""
    media_info: NotRequired["capo_mediaconnect.types.ndi_media_info.NdiMediaInfo"]
    """<p> Detailed information about the media streams (video, audio, and so on) that are part of the active NDI source. </p>"""
    messages: NotRequired[
        "capo_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"
    ]
    """<p> Any status messages or error codes related to the NDI source and its metadata. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiSourceMetadataInfo) -> dict:
    out: dict = {}
    if "active_source" in value:
        import capo_mediaconnect.types.ndi_source_info

        out["activeSource"] = capo_mediaconnect.types.ndi_source_info.serialize_json(
            value["active_source"]
        )
    if "discovered_sources" in value:
        import capo_mediaconnect.types.__list_of_ndi_source_info

        out["discoveredSources"] = (
            capo_mediaconnect.types.__list_of_ndi_source_info.serialize_json(
                value["discovered_sources"]
            )
        )
    if "media_info" in value:
        import capo_mediaconnect.types.ndi_media_info

        out["mediaInfo"] = capo_mediaconnect.types.ndi_media_info.serialize_json(
            value["media_info"]
        )
    if "messages" in value:
        import capo_mediaconnect.types.__list_of_message_detail

        out["messages"] = (
            capo_mediaconnect.types.__list_of_message_detail.serialize_json(
                value["messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> NdiSourceMetadataInfo:
    out: NdiSourceMetadataInfo = {}  # type: ignore[typeddict-item]
    if "activeSource" in data:
        import capo_mediaconnect.types.ndi_source_info

        out["active_source"] = capo_mediaconnect.types.ndi_source_info.deserialize_json(
            data["activeSource"]
        )
    if "discoveredSources" in data:
        import capo_mediaconnect.types.__list_of_ndi_source_info

        out["discovered_sources"] = (
            capo_mediaconnect.types.__list_of_ndi_source_info.deserialize_json(
                data["discoveredSources"]
            )
        )
    if "mediaInfo" in data:
        import capo_mediaconnect.types.ndi_media_info

        out["media_info"] = capo_mediaconnect.types.ndi_media_info.deserialize_json(
            data["mediaInfo"]
        )
    if "messages" in data:
        import capo_mediaconnect.types.__list_of_message_detail

        out["messages"] = (
            capo_mediaconnect.types.__list_of_message_detail.deserialize_json(
                data["messages"]
            )
        )
    return out
