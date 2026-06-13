"""Generated from Smithy shape ``com.amazonaws.quicksight#CurrencyDisplayFormatConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.currency_code
    import aws_sdk_quicksight.types.decimal_places_configuration
    import aws_sdk_quicksight.types.negative_value_configuration
    import aws_sdk_quicksight.types.null_value_format_configuration
    import aws_sdk_quicksight.types.number_scale
    import aws_sdk_quicksight.types.numeric_separator_configuration
    import aws_sdk_quicksight.types.prefix
    import aws_sdk_quicksight.types.suffix


class CurrencyDisplayFormatConfiguration(TypedDict):
    prefix: NotRequired["aws_sdk_quicksight.types.prefix.Prefix"]
    """<p>Determines the prefix value of the currency format.</p>"""
    suffix: NotRequired["aws_sdk_quicksight.types.suffix.Suffix"]
    """<p>Determines the suffix value of the currency format.</p>"""
    separator_configuration: NotRequired[
        "aws_sdk_quicksight.types.numeric_separator_configuration.NumericSeparatorConfiguration"
    ]
    """<p>The options that determine the numeric separator configuration.</p>"""
    symbol: NotRequired["aws_sdk_quicksight.types.currency_code.CurrencyCode"]
    """<p>Determines the symbol for the currency format.</p>"""
    decimal_places_configuration: NotRequired[
        "aws_sdk_quicksight.types.decimal_places_configuration.DecimalPlacesConfiguration"
    ]
    """<p>The option that determines the decimal places configuration.</p>"""
    number_scale: NotRequired["aws_sdk_quicksight.types.number_scale.NumberScale"]
    """<p>Determines the number scale value for the currency format.</p>"""
    negative_value_configuration: NotRequired[
        "aws_sdk_quicksight.types.negative_value_configuration.NegativeValueConfiguration"
    ]
    """<p>The options that determine the negative value configuration.</p>"""
    null_value_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.null_value_format_configuration.NullValueFormatConfiguration"
    ]
    """<p>The options that determine the null value format configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CurrencyDisplayFormatConfiguration) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "suffix" in value:
        out["Suffix"] = value["suffix"]
    if "separator_configuration" in value:
        import aws_sdk_quicksight.types.numeric_separator_configuration

        out["SeparatorConfiguration"] = (
            aws_sdk_quicksight.types.numeric_separator_configuration.serialize_json(
                value["separator_configuration"]
            )
        )
    if "symbol" in value:
        out["Symbol"] = value["symbol"]
    if "decimal_places_configuration" in value:
        import aws_sdk_quicksight.types.decimal_places_configuration

        out["DecimalPlacesConfiguration"] = (
            aws_sdk_quicksight.types.decimal_places_configuration.serialize_json(
                value["decimal_places_configuration"]
            )
        )
    if "number_scale" in value:
        import aws_sdk_quicksight.types.number_scale

        out["NumberScale"] = aws_sdk_quicksight.types.number_scale.serialize_json(
            value["number_scale"]
        )
    if "negative_value_configuration" in value:
        import aws_sdk_quicksight.types.negative_value_configuration

        out["NegativeValueConfiguration"] = (
            aws_sdk_quicksight.types.negative_value_configuration.serialize_json(
                value["negative_value_configuration"]
            )
        )
    if "null_value_format_configuration" in value:
        import aws_sdk_quicksight.types.null_value_format_configuration

        out["NullValueFormatConfiguration"] = (
            aws_sdk_quicksight.types.null_value_format_configuration.serialize_json(
                value["null_value_format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CurrencyDisplayFormatConfiguration:
    out: CurrencyDisplayFormatConfiguration = {}  # type: ignore[typeddict-item]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "Suffix" in data:
        out["suffix"] = data["Suffix"]
    if "SeparatorConfiguration" in data:
        import aws_sdk_quicksight.types.numeric_separator_configuration

        out["separator_configuration"] = (
            aws_sdk_quicksight.types.numeric_separator_configuration.deserialize_json(
                data["SeparatorConfiguration"]
            )
        )
    if "Symbol" in data:
        out["symbol"] = data["Symbol"]
    if "DecimalPlacesConfiguration" in data:
        import aws_sdk_quicksight.types.decimal_places_configuration

        out["decimal_places_configuration"] = (
            aws_sdk_quicksight.types.decimal_places_configuration.deserialize_json(
                data["DecimalPlacesConfiguration"]
            )
        )
    if "NumberScale" in data:
        import aws_sdk_quicksight.types.number_scale

        out["number_scale"] = aws_sdk_quicksight.types.number_scale.deserialize_json(
            data["NumberScale"]
        )
    if "NegativeValueConfiguration" in data:
        import aws_sdk_quicksight.types.negative_value_configuration

        out["negative_value_configuration"] = (
            aws_sdk_quicksight.types.negative_value_configuration.deserialize_json(
                data["NegativeValueConfiguration"]
            )
        )
    if "NullValueFormatConfiguration" in data:
        import aws_sdk_quicksight.types.null_value_format_configuration

        out["null_value_format_configuration"] = (
            aws_sdk_quicksight.types.null_value_format_configuration.deserialize_json(
                data["NullValueFormatConfiguration"]
            )
        )
    return out
