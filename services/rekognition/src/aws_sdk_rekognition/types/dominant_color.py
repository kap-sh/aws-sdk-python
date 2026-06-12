"""Generated from Smithy shape ``com.amazonaws.rekognition#DominantColor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.u_integer


class DominantColor(TypedDict):
    red: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>The Red RGB value for a dominant color.</p>"""
    blue: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>The Blue RGB value for a dominant color.</p>"""
    green: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>The Green RGB value for a dominant color.</p>"""
    hex_code: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The Hex code equivalent of the RGB values for a dominant color.</p>"""
    css_color: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The CSS color name of a dominant color.</p>"""
    simplified_color: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>One of 12 simplified color names applied to a dominant color.</p>"""
    pixel_percent: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The percentage of image pixels that have a given dominant color.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DominantColor) -> dict:
    out: dict = {}
    if "red" in value:
        out["Red"] = value["red"]
    if "blue" in value:
        out["Blue"] = value["blue"]
    if "green" in value:
        out["Green"] = value["green"]
    if "hex_code" in value:
        out["HexCode"] = value["hex_code"]
    if "css_color" in value:
        out["CSSColor"] = value["css_color"]
    if "simplified_color" in value:
        out["SimplifiedColor"] = value["simplified_color"]
    if "pixel_percent" in value:
        out["PixelPercent"] = value["pixel_percent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DominantColor:
    out: DominantColor = {}  # type: ignore[typeddict-item]
    if "Red" in data:
        out["red"] = data["Red"]
    if "Blue" in data:
        out["blue"] = data["Blue"]
    if "Green" in data:
        out["green"] = data["Green"]
    if "HexCode" in data:
        out["hex_code"] = data["HexCode"]
    if "CSSColor" in data:
        out["css_color"] = data["CSSColor"]
    if "SimplifiedColor" in data:
        out["simplified_color"] = data["SimplifiedColor"]
    if "PixelPercent" in data:
        out["pixel_percent"] = data["PixelPercent"]
    return out
