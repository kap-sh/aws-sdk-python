"""Generated from Smithy shape ``com.amazonaws.quicksight#PanelTitleOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.horizontal_text_alignment
    import aws_sdk_quicksight.types.visibility


class PanelTitleOptions(TypedDict, closed=True):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not panel titles are displayed.</p>"""
    font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    horizontal_text_alignment: NotRequired[
        "aws_sdk_quicksight.types.horizontal_text_alignment.HorizontalTextAlignment"
    ]
    """<p>Sets the horizontal text alignment of the title within each panel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PanelTitleOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["FontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["font_configuration"]
            )
        )
    if "horizontal_text_alignment" in value:
        import aws_sdk_quicksight.types.horizontal_text_alignment

        out["HorizontalTextAlignment"] = (
            aws_sdk_quicksight.types.horizontal_text_alignment.serialize_json(
                value["horizontal_text_alignment"]
            )
        )
    return out


def deserialize_json(data: dict) -> PanelTitleOptions:
    out: PanelTitleOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "FontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["FontConfiguration"]
            )
        )
    if "HorizontalTextAlignment" in data:
        import aws_sdk_quicksight.types.horizontal_text_alignment

        out["horizontal_text_alignment"] = (
            aws_sdk_quicksight.types.horizontal_text_alignment.deserialize_json(
                data["HorizontalTextAlignment"]
            )
        )
    return out
