"""Generated from Smithy shape ``com.amazonaws.medialive#ThumbnailConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.thumbnail_state


class ThumbnailConfiguration(TypedDict):
    state: NotRequired["aws_sdk_medialive.types.thumbnail_state.ThumbnailState"]
    """Enables the thumbnail feature. The feature generates thumbnails of the incoming video in each pipeline in the channel. AUTO turns the feature on, DISABLE turns the feature off."""


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailConfiguration) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_medialive.types.thumbnail_state

        out["state"] = aws_sdk_medialive.types.thumbnail_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> ThumbnailConfiguration:
    out: ThumbnailConfiguration = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_medialive.types.thumbnail_state

        out["state"] = aws_sdk_medialive.types.thumbnail_state.deserialize_json(
            data["state"]
        )
    return out
