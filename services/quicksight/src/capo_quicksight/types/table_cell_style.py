"""Generated from Smithy shape ``com.amazonaws.quicksight#TableCellStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.font_configuration
    import capo_quicksight.types.global_table_border_options
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.horizontal_text_alignment
    import capo_quicksight.types.table_field_height
    import capo_quicksight.types.text_wrap
    import capo_quicksight.types.vertical_text_alignment
    import capo_quicksight.types.visibility


class TableCellStyle(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the table cells.</p>"""
    font_configuration: NotRequired[
        "capo_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The font configuration of the table cells.</p>"""
    text_wrap: NotRequired["capo_quicksight.types.text_wrap.TextWrap"]
    """<p>The text wrap (none, wrap) for the table cells.</p>"""
    horizontal_text_alignment: NotRequired[
        "capo_quicksight.types.horizontal_text_alignment.HorizontalTextAlignment"
    ]
    """<p>The horizontal text alignment (left, center, right, auto) for the table cells.</p>"""
    vertical_text_alignment: NotRequired[
        "capo_quicksight.types.vertical_text_alignment.VerticalTextAlignment"
    ]
    """<p>The vertical text alignment (top, middle, bottom) for the table cells.</p>"""
    background_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The background color for the table cells.</p>"""
    height: NotRequired["capo_quicksight.types.table_field_height.TableFieldHeight"]
    """<p>The height color for the table cells.</p>"""
    border: NotRequired[
        "capo_quicksight.types.global_table_border_options.GlobalTableBorderOptions"
    ]
    """<p>The borders for the table cells.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableCellStyle) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "font_configuration" in value:
        import capo_quicksight.types.font_configuration

        out["FontConfiguration"] = (
            capo_quicksight.types.font_configuration.serialize_json(
                value["font_configuration"]
            )
        )
    if "text_wrap" in value:
        import capo_quicksight.types.text_wrap

        out["TextWrap"] = capo_quicksight.types.text_wrap.serialize_json(
            value["text_wrap"]
        )
    if "horizontal_text_alignment" in value:
        import capo_quicksight.types.horizontal_text_alignment

        out["HorizontalTextAlignment"] = (
            capo_quicksight.types.horizontal_text_alignment.serialize_json(
                value["horizontal_text_alignment"]
            )
        )
    if "vertical_text_alignment" in value:
        import capo_quicksight.types.vertical_text_alignment

        out["VerticalTextAlignment"] = (
            capo_quicksight.types.vertical_text_alignment.serialize_json(
                value["vertical_text_alignment"]
            )
        )
    if "background_color" in value:
        out["BackgroundColor"] = value["background_color"]
    if "height" in value:
        out["Height"] = value["height"]
    if "border" in value:
        import capo_quicksight.types.global_table_border_options

        out["Border"] = (
            capo_quicksight.types.global_table_border_options.serialize_json(
                value["border"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableCellStyle:
    out: TableCellStyle = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "FontConfiguration" in data:
        import capo_quicksight.types.font_configuration

        out["font_configuration"] = (
            capo_quicksight.types.font_configuration.deserialize_json(
                data["FontConfiguration"]
            )
        )
    if "TextWrap" in data:
        import capo_quicksight.types.text_wrap

        out["text_wrap"] = capo_quicksight.types.text_wrap.deserialize_json(
            data["TextWrap"]
        )
    if "HorizontalTextAlignment" in data:
        import capo_quicksight.types.horizontal_text_alignment

        out["horizontal_text_alignment"] = (
            capo_quicksight.types.horizontal_text_alignment.deserialize_json(
                data["HorizontalTextAlignment"]
            )
        )
    if "VerticalTextAlignment" in data:
        import capo_quicksight.types.vertical_text_alignment

        out["vertical_text_alignment"] = (
            capo_quicksight.types.vertical_text_alignment.deserialize_json(
                data["VerticalTextAlignment"]
            )
        )
    if "BackgroundColor" in data:
        out["background_color"] = data["BackgroundColor"]
    if "Height" in data:
        out["height"] = data["Height"]
    if "Border" in data:
        import capo_quicksight.types.global_table_border_options

        out["border"] = (
            capo_quicksight.types.global_table_border_options.deserialize_json(
                data["Border"]
            )
        )
    return out
