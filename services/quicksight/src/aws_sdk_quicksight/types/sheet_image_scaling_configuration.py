"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageScalingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_image_scaling_type


class SheetImageScalingConfiguration(TypedDict):
    scaling_type: NotRequired[
        "aws_sdk_quicksight.types.sheet_image_scaling_type.SheetImageScalingType"
    ]
    """<p>The scaling option to use when fitting the image inside the container.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>SCALE_TO_WIDTH</code>: The image takes up the entire width of the container. The image aspect ratio is preserved.</p> </li> <li> <p> <code>SCALE_TO_HEIGHT</code>: The image takes up the entire height of the container. The image aspect ratio is preserved.</p> </li> <li> <p> <code>SCALE_TO_CONTAINER</code>: The image takes up the entire width and height of the container. The image aspect ratio is not preserved.</p> </li> <li> <p> <code>SCALE_NONE</code>: The image is displayed in its original size and is not scaled to the container.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageScalingConfiguration) -> dict:
    out: dict = {}
    if "scaling_type" in value:
        import aws_sdk_quicksight.types.sheet_image_scaling_type

        out["ScalingType"] = (
            aws_sdk_quicksight.types.sheet_image_scaling_type.serialize_json(
                value["scaling_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetImageScalingConfiguration:
    out: SheetImageScalingConfiguration = {}  # type: ignore[typeddict-item]
    if "ScalingType" in data:
        import aws_sdk_quicksight.types.sheet_image_scaling_type

        out["scaling_type"] = (
            aws_sdk_quicksight.types.sheet_image_scaling_type.deserialize_json(
                data["ScalingType"]
            )
        )
    return out
