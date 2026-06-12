"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_status
    import aws_sdk_imagebuilder.types.non_empty_string


class ImageState(TypedDict):
    status: NotRequired["aws_sdk_imagebuilder.types.image_status.ImageStatus"]
    """<p>The status of the image.</p>"""
    reason: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the status of the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_imagebuilder.types.image_status

        out["status"] = aws_sdk_imagebuilder.types.image_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ImageState:
    out: ImageState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_imagebuilder.types.image_status

        out["status"] = aws_sdk_imagebuilder.types.image_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
