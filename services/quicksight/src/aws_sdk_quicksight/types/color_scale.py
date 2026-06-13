"""Generated from Smithy shape ``com.amazonaws.quicksight#ColorScale``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.color_fill_type
    import aws_sdk_quicksight.types.color_scale_color_list
    import aws_sdk_quicksight.types.data_color


class ColorScale(TypedDict):
    colors: "aws_sdk_quicksight.types.color_scale_color_list.ColorScaleColorList"
    """<p>Determines the list of colors that are applied to the visual.</p>"""
    color_fill_type: "aws_sdk_quicksight.types.color_fill_type.ColorFillType"
    """<p>Determines the color fill type.</p>"""
    null_value_color: NotRequired["aws_sdk_quicksight.types.data_color.DataColor"]
    """<p>Determines the color that is applied to null values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColorScale) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.color_scale_color_list

    out["Colors"] = aws_sdk_quicksight.types.color_scale_color_list.serialize_json(
        value["colors"]
    )
    import aws_sdk_quicksight.types.color_fill_type

    out["ColorFillType"] = aws_sdk_quicksight.types.color_fill_type.serialize_json(
        value["color_fill_type"]
    )
    if "null_value_color" in value:
        import aws_sdk_quicksight.types.data_color

        out["NullValueColor"] = aws_sdk_quicksight.types.data_color.serialize_json(
            value["null_value_color"]
        )
    return out


def deserialize_json(data: dict) -> ColorScale:
    out: ColorScale = {}  # type: ignore[typeddict-item]
    if "Colors" in data:
        import aws_sdk_quicksight.types.color_scale_color_list

        out["colors"] = (
            aws_sdk_quicksight.types.color_scale_color_list.deserialize_json(
                data["Colors"]
            )
        )
    else:
        raise DeserializationError("ColorScale.colors required")
    if "ColorFillType" in data:
        import aws_sdk_quicksight.types.color_fill_type

        out["color_fill_type"] = (
            aws_sdk_quicksight.types.color_fill_type.deserialize_json(
                data["ColorFillType"]
            )
        )
    else:
        raise DeserializationError("ColorScale.color_fill_type required")
    if "NullValueColor" in data:
        import aws_sdk_quicksight.types.data_color

        out["null_value_color"] = aws_sdk_quicksight.types.data_color.deserialize_json(
            data["NullValueColor"]
        )
    return out
