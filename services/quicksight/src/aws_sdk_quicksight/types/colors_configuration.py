"""Generated from Smithy shape ``com.amazonaws.quicksight#ColorsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_colors_list


class ColorsConfiguration(TypedDict, closed=True):
    custom_colors: NotRequired[
        "aws_sdk_quicksight.types.custom_colors_list.CustomColorsList"
    ]
    """<p>A list of up to 50 custom colors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColorsConfiguration) -> dict:
    out: dict = {}
    if "custom_colors" in value:
        import aws_sdk_quicksight.types.custom_colors_list

        out["CustomColors"] = (
            aws_sdk_quicksight.types.custom_colors_list.serialize_json(
                value["custom_colors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColorsConfiguration:
    out: ColorsConfiguration = {}  # type: ignore[typeddict-item]
    if "CustomColors" in data:
        import aws_sdk_quicksight.types.custom_colors_list

        out["custom_colors"] = (
            aws_sdk_quicksight.types.custom_colors_list.deserialize_json(
                data["CustomColors"]
            )
        )
    return out
