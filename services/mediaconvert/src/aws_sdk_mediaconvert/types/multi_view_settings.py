"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MultiViewSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.multi_view_input


class MultiViewSettings(TypedDict, closed=True):
    input: NotRequired["aws_sdk_mediaconvert.types.multi_view_input.MultiViewInput"]
    """Input settings for MultiView Settings. You can include exactly one input as enhancement layer."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiViewSettings) -> dict:
    out: dict = {}
    if "input" in value:
        import aws_sdk_mediaconvert.types.multi_view_input

        out["input"] = aws_sdk_mediaconvert.types.multi_view_input.serialize_json(
            value["input"]
        )
    return out


def deserialize_json(data: dict) -> MultiViewSettings:
    out: MultiViewSettings = {}  # type: ignore[typeddict-item]
    if "input" in data:
        import aws_sdk_mediaconvert.types.multi_view_input

        out["input"] = aws_sdk_mediaconvert.types.multi_view_input.deserialize_json(
            data["input"]
        )
    return out
