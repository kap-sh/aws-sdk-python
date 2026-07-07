"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericFormatConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.currency_display_format_configuration
    import aws_sdk_quicksight.types.number_display_format_configuration
    import aws_sdk_quicksight.types.percentage_display_format_configuration


class NumericFormatConfiguration(TypedDict, closed=True):
    number_display_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.number_display_format_configuration.NumberDisplayFormatConfiguration"
    ]
    """<p>The options that determine the number display format configuration.</p>"""
    currency_display_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.currency_display_format_configuration.CurrencyDisplayFormatConfiguration"
    ]
    """<p>The options that determine the currency display format configuration.</p>"""
    percentage_display_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.percentage_display_format_configuration.PercentageDisplayFormatConfiguration"
    ]
    """<p>The options that determine the percentage display format configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericFormatConfiguration) -> dict:
    out: dict = {}
    if "number_display_format_configuration" in value:
        import aws_sdk_quicksight.types.number_display_format_configuration

        out["NumberDisplayFormatConfiguration"] = (
            aws_sdk_quicksight.types.number_display_format_configuration.serialize_json(
                value["number_display_format_configuration"]
            )
        )
    if "currency_display_format_configuration" in value:
        import aws_sdk_quicksight.types.currency_display_format_configuration

        out["CurrencyDisplayFormatConfiguration"] = (
            aws_sdk_quicksight.types.currency_display_format_configuration.serialize_json(
                value["currency_display_format_configuration"]
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


def deserialize_json(data: dict) -> NumericFormatConfiguration:
    out: NumericFormatConfiguration = {}  # type: ignore[typeddict-item]
    if "NumberDisplayFormatConfiguration" in data:
        import aws_sdk_quicksight.types.number_display_format_configuration

        out["number_display_format_configuration"] = (
            aws_sdk_quicksight.types.number_display_format_configuration.deserialize_json(
                data["NumberDisplayFormatConfiguration"]
            )
        )
    if "CurrencyDisplayFormatConfiguration" in data:
        import aws_sdk_quicksight.types.currency_display_format_configuration

        out["currency_display_format_configuration"] = (
            aws_sdk_quicksight.types.currency_display_format_configuration.deserialize_json(
                data["CurrencyDisplayFormatConfiguration"]
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
