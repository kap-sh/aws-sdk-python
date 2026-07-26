"""Generated from Smithy shape ``com.amazonaws.medialive#ThumbnailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.thumbnail_state


class ThumbnailConfiguration(TypedDict, closed=True):
    state: NotRequired["capo_medialive.types.thumbnail_state.ThumbnailState"]
    """Enables the thumbnail feature. The feature generates thumbnails of the incoming video in each pipeline in the channel. AUTO turns the feature on, DISABLE turns the feature off."""


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailConfiguration) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_medialive.types.thumbnail_state

        out["state"] = capo_medialive.types.thumbnail_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> ThumbnailConfiguration:
    out: ThumbnailConfiguration = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_medialive.types.thumbnail_state

        out["state"] = capo_medialive.types.thumbnail_state.deserialize_json(
            data["state"]
        )
    return out
