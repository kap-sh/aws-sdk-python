"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CompositionThumbnailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.thumbnail_interval_seconds
    import capo_ivs_realtime.types.thumbnail_storage_type_list


class CompositionThumbnailConfiguration(TypedDict, closed=True):
    target_interval_seconds: NotRequired[
        "capo_ivs_realtime.types.thumbnail_interval_seconds.ThumbnailIntervalSeconds"
    ]
    """<p>The targeted thumbnail-generation interval in seconds. Default: 60.</p>"""
    storage: NotRequired[
        "capo_ivs_realtime.types.thumbnail_storage_type_list.ThumbnailStorageTypeList"
    ]
    """<p>Indicates the format in which thumbnails are recorded. <code>SEQUENTIAL</code> records all generated thumbnails in a serial manner, to the media/thumbnails/(width)x(height) directory, where (width) and (height) are the width and height of the thumbnail. <code>LATEST</code> saves the latest thumbnail in media/latest_thumbnail/(width)x(height)/thumb.jpg and overwrites it at the interval specified by <code>targetIntervalSeconds</code>. You can enable both <code>SEQUENTIAL</code> and <code>LATEST</code>. Default: <code>SEQUENTIAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositionThumbnailConfiguration) -> dict:
    out: dict = {}
    if "target_interval_seconds" in value:
        out["targetIntervalSeconds"] = value["target_interval_seconds"]
    if "storage" in value:
        import capo_ivs_realtime.types.thumbnail_storage_type_list

        out["storage"] = (
            capo_ivs_realtime.types.thumbnail_storage_type_list.serialize_json(
                value["storage"]
            )
        )
    return out


def deserialize_json(data: dict) -> CompositionThumbnailConfiguration:
    out: CompositionThumbnailConfiguration = {}  # type: ignore[typeddict-item]
    if "targetIntervalSeconds" in data:
        out["target_interval_seconds"] = data["targetIntervalSeconds"]
    if "storage" in data:
        import capo_ivs_realtime.types.thumbnail_storage_type_list

        out["storage"] = (
            capo_ivs_realtime.types.thumbnail_storage_type_list.deserialize_json(
                data["storage"]
            )
        )
    return out
