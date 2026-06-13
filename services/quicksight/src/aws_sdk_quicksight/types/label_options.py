"""Generated from Smithy shape ``com.amazonaws.quicksight#LabelOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.visibility


class LabelOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not the label is visible.</p>"""
    font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The font configuration of the label.</p>"""
    custom_label: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The text for the label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LabelOptions) -> dict:
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
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
    return out


def deserialize_json(data: dict) -> LabelOptions:
    out: LabelOptions = {}  # type: ignore[typeddict-item]
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
    if "CustomLabel" in data:
        out["custom_label"] = data["CustomLabel"]
    return out
