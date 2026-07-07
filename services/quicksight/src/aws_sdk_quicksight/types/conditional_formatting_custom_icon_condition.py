"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingCustomIconCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_custom_icon_options
    import aws_sdk_quicksight.types.conditional_formatting_icon_display_configuration
    import aws_sdk_quicksight.types.expression
    import aws_sdk_quicksight.types.hex_color


class ConditionalFormattingCustomIconCondition(TypedDict, closed=True):
    expression: "aws_sdk_quicksight.types.expression.Expression"
    """<p>The expression that determines the condition of the icon set.</p>"""
    icon_options: "aws_sdk_quicksight.types.conditional_formatting_custom_icon_options.ConditionalFormattingCustomIconOptions"
    """<p>Custom icon options for an icon set.</p>"""
    color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>Determines the color of the icon.</p>"""
    display_configuration: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_icon_display_configuration.ConditionalFormattingIconDisplayConfiguration"
    ]
    """<p>Determines the icon display configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingCustomIconCondition) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    import aws_sdk_quicksight.types.conditional_formatting_custom_icon_options

    out["IconOptions"] = (
        aws_sdk_quicksight.types.conditional_formatting_custom_icon_options.serialize_json(
            value["icon_options"]
        )
    )
    if "color" in value:
        out["Color"] = value["color"]
    if "display_configuration" in value:
        import aws_sdk_quicksight.types.conditional_formatting_icon_display_configuration

        out["DisplayConfiguration"] = (
            aws_sdk_quicksight.types.conditional_formatting_icon_display_configuration.serialize_json(
                value["display_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingCustomIconCondition:
    out: ConditionalFormattingCustomIconCondition = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError(
            "ConditionalFormattingCustomIconCondition.expression required"
        )
    if "IconOptions" in data:
        import aws_sdk_quicksight.types.conditional_formatting_custom_icon_options

        out["icon_options"] = (
            aws_sdk_quicksight.types.conditional_formatting_custom_icon_options.deserialize_json(
                data["IconOptions"]
            )
        )
    else:
        raise DeserializationError(
            "ConditionalFormattingCustomIconCondition.icon_options required"
        )
    if "Color" in data:
        out["color"] = data["Color"]
    if "DisplayConfiguration" in data:
        import aws_sdk_quicksight.types.conditional_formatting_icon_display_configuration

        out["display_configuration"] = (
            aws_sdk_quicksight.types.conditional_formatting_icon_display_configuration.deserialize_json(
                data["DisplayConfiguration"]
            )
        )
    return out
