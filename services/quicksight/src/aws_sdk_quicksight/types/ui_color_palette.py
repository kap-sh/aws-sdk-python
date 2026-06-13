"""Generated from Smithy shape ``com.amazonaws.quicksight#UIColorPalette``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color


class UIColorPalette(TypedDict):
    primary_foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color of text and other foreground elements that appear over the primary background regions, such as grid lines, borders, table banding, icons, and so on.</p>"""
    primary_background: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The background color that applies to visuals and other high emphasis UI.</p>"""
    secondary_foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color that applies to any sheet title, sheet control text, or UI that appears over the secondary background.</p>"""
    secondary_background: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The background color that applies to the sheet background and sheet controls.</p>"""
    accent: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>This color is that applies to selected states and buttons.</p>"""
    accent_foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color that applies to any text or other elements that appear over the accent color.</p>"""
    danger: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color that applies to error messages.</p>"""
    danger_foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color that applies to any text or other elements that appear over the error color.</p>"""
    warning: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>This color that applies to warning and informational messages.</p>"""
    warning_foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color that applies to any text or other elements that appear over the warning color.</p>"""
    success: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color that applies to success messages, for example the check mark for a successful download.</p>"""
    success_foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color that applies to any text or other elements that appear over the success color.</p>"""
    dimension: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color that applies to the names of fields that are identified as dimensions.</p>"""
    dimension_foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color that applies to any text or other elements that appear over the dimension color.</p>"""
    measure: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color that applies to the names of fields that are identified as measures.</p>"""
    measure_foreground: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color that applies to any text or other elements that appear over the measure color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UIColorPalette) -> dict:
    out: dict = {}
    if "primary_foreground" in value:
        out["PrimaryForeground"] = value["primary_foreground"]
    if "primary_background" in value:
        out["PrimaryBackground"] = value["primary_background"]
    if "secondary_foreground" in value:
        out["SecondaryForeground"] = value["secondary_foreground"]
    if "secondary_background" in value:
        out["SecondaryBackground"] = value["secondary_background"]
    if "accent" in value:
        out["Accent"] = value["accent"]
    if "accent_foreground" in value:
        out["AccentForeground"] = value["accent_foreground"]
    if "danger" in value:
        out["Danger"] = value["danger"]
    if "danger_foreground" in value:
        out["DangerForeground"] = value["danger_foreground"]
    if "warning" in value:
        out["Warning"] = value["warning"]
    if "warning_foreground" in value:
        out["WarningForeground"] = value["warning_foreground"]
    if "success" in value:
        out["Success"] = value["success"]
    if "success_foreground" in value:
        out["SuccessForeground"] = value["success_foreground"]
    if "dimension" in value:
        out["Dimension"] = value["dimension"]
    if "dimension_foreground" in value:
        out["DimensionForeground"] = value["dimension_foreground"]
    if "measure" in value:
        out["Measure"] = value["measure"]
    if "measure_foreground" in value:
        out["MeasureForeground"] = value["measure_foreground"]
    return out


def deserialize_json(data: dict) -> UIColorPalette:
    out: UIColorPalette = {}  # type: ignore[typeddict-item]
    if "PrimaryForeground" in data:
        out["primary_foreground"] = data["PrimaryForeground"]
    if "PrimaryBackground" in data:
        out["primary_background"] = data["PrimaryBackground"]
    if "SecondaryForeground" in data:
        out["secondary_foreground"] = data["SecondaryForeground"]
    if "SecondaryBackground" in data:
        out["secondary_background"] = data["SecondaryBackground"]
    if "Accent" in data:
        out["accent"] = data["Accent"]
    if "AccentForeground" in data:
        out["accent_foreground"] = data["AccentForeground"]
    if "Danger" in data:
        out["danger"] = data["Danger"]
    if "DangerForeground" in data:
        out["danger_foreground"] = data["DangerForeground"]
    if "Warning" in data:
        out["warning"] = data["Warning"]
    if "WarningForeground" in data:
        out["warning_foreground"] = data["WarningForeground"]
    if "Success" in data:
        out["success"] = data["Success"]
    if "SuccessForeground" in data:
        out["success_foreground"] = data["SuccessForeground"]
    if "Dimension" in data:
        out["dimension"] = data["Dimension"]
    if "DimensionForeground" in data:
        out["dimension_foreground"] = data["DimensionForeground"]
    if "Measure" in data:
        out["measure"] = data["Measure"]
    if "MeasureForeground" in data:
        out["measure_foreground"] = data["MeasureForeground"]
    return out
