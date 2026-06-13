"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparisonFormatConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.number_display_format_configuration
    import aws_sdk_quicksight.types.percentage_display_format_configuration


class ComparisonFormatConfiguration(TypedDict):
    number_display_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.number_display_format_configuration.NumberDisplayFormatConfiguration"
    ]
    """<p>The number display format.</p>"""
    percentage_display_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.percentage_display_format_configuration.PercentageDisplayFormatConfiguration"
    ]
    """<p>The percentage display format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonFormatConfiguration) -> dict:
    out: dict = {}
    if "number_display_format_configuration" in value:
        import aws_sdk_quicksight.types.number_display_format_configuration

        out["NumberDisplayFormatConfiguration"] = (
            aws_sdk_quicksight.types.number_display_format_configuration.serialize_json(
                value["number_display_format_configuration"]
            )
        )
    if "percentage_display_format_configuration" in value:
        import aws_sdk_quicksight.types.percentage_display_format_configuration

        out["PercentageDisplayFormatConfiguration"] = (
            aws_sdk_quicksight.types.percentage_display_format_configuration.serialize_json(
                value["percentage_display_format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComparisonFormatConfiguration:
    out: ComparisonFormatConfiguration = {}  # type: ignore[typeddict-item]
    if "NumberDisplayFormatConfiguration" in data:
        import aws_sdk_quicksight.types.number_display_format_configuration

        out["number_display_format_configuration"] = (
            aws_sdk_quicksight.types.number_display_format_configuration.deserialize_json(
                data["NumberDisplayFormatConfiguration"]
            )
        )
    if "PercentageDisplayFormatConfiguration" in data:
        import aws_sdk_quicksight.types.percentage_display_format_configuration

        out["percentage_display_format_configuration"] = (
            aws_sdk_quicksight.types.percentage_display_format_configuration.deserialize_json(
                data["PercentageDisplayFormatConfiguration"]
            )
        )
    return out
