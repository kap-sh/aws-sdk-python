"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiSourceMetadataInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_message_detail
    import aws_sdk_mediaconnect.types.__list_of_ndi_source_info
    import aws_sdk_mediaconnect.types.ndi_media_info
    import aws_sdk_mediaconnect.types.ndi_source_info


class NdiSourceMetadataInfo(TypedDict):
    active_source: NotRequired[
        "aws_sdk_mediaconnect.types.ndi_source_info.NdiSourceInfo"
    ]
    """<p> The connected NDI sender that's currently sending source content to the flow's NDI source. </p>"""
    discovered_sources: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_ndi_source_info.__listOfNdiSourceInfo"
    ]
    """<p> A list of the available upstream NDI senders aggregated from all of your configured discovery servers. </p>"""
    media_info: NotRequired["aws_sdk_mediaconnect.types.ndi_media_info.NdiMediaInfo"]
    """<p> Detailed information about the media streams (video, audio, and so on) that are part of the active NDI source. </p>"""
    messages: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"
    ]
    """<p> Any status messages or error codes related to the NDI source and its metadata. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiSourceMetadataInfo) -> dict:
    out: dict = {}
    if "active_source" in value:
        import aws_sdk_mediaconnect.types.ndi_source_info

        out["activeSource"] = aws_sdk_mediaconnect.types.ndi_source_info.serialize_json(
            value["active_source"]
        )
    if "discovered_sources" in value:
        import aws_sdk_mediaconnect.types.__list_of_ndi_source_info

        out["discoveredSources"] = (
            aws_sdk_mediaconnect.types.__list_of_ndi_source_info.serialize_json(
                value["discovered_sources"]
            )
        )
    if "media_info" in value:
        import aws_sdk_mediaconnect.types.ndi_media_info

        out["mediaInfo"] = aws_sdk_mediaconnect.types.ndi_media_info.serialize_json(
            value["media_info"]
        )
    if "messages" in value:
        import aws_sdk_mediaconnect.types.__list_of_message_detail

        out["messages"] = (
            aws_sdk_mediaconnect.types.__list_of_message_detail.serialize_json(
                value["messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> NdiSourceMetadataInfo:
    out: NdiSourceMetadataInfo = {}  # type: ignore[typeddict-item]
    if "activeSource" in data:
        import aws_sdk_mediaconnect.types.ndi_source_info

        out["active_source"] = (
            aws_sdk_mediaconnect.types.ndi_source_info.deserialize_json(
                data["activeSource"]
            )
        )
    if "discoveredSources" in data:
        import aws_sdk_mediaconnect.types.__list_of_ndi_source_info

        out["discovered_sources"] = (
            aws_sdk_mediaconnect.types.__list_of_ndi_source_info.deserialize_json(
                data["discoveredSources"]
            )
        )
    if "mediaInfo" in data:
        import aws_sdk_mediaconnect.types.ndi_media_info

        out["media_info"] = aws_sdk_mediaconnect.types.ndi_media_info.deserialize_json(
            data["mediaInfo"]
        )
    if "messages" in data:
        import aws_sdk_mediaconnect.types.__list_of_message_detail

        out["messages"] = (
            aws_sdk_mediaconnect.types.__list_of_message_detail.deserialize_json(
                data["messages"]
            )
        )
    return out
