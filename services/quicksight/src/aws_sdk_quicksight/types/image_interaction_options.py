"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageInteractionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.image_menu_option


class ImageInteractionOptions(TypedDict, closed=True):
    image_menu_option: NotRequired[
        "aws_sdk_quicksight.types.image_menu_option.ImageMenuOption"
    ]
    """<p>The menu options for the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageInteractionOptions) -> dict:
    out: dict = {}
    if "image_menu_option" in value:
        import aws_sdk_quicksight.types.image_menu_option

        out["ImageMenuOption"] = (
            aws_sdk_quicksight.types.image_menu_option.serialize_json(
                value["image_menu_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageInteractionOptions:
    out: ImageInteractionOptions = {}  # type: ignore[typeddict-item]
    if "ImageMenuOption" in data:
        import aws_sdk_quicksight.types.image_menu_option

        out["image_menu_option"] = (
            aws_sdk_quicksight.types.image_menu_option.deserialize_json(
                data["ImageMenuOption"]
            )
        )
    return out
