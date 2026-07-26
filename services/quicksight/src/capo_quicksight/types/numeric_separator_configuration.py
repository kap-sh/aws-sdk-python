"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericSeparatorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.numeric_separator_symbol
    import capo_quicksight.types.thousand_separator_options


class NumericSeparatorConfiguration(TypedDict, closed=True):
    decimal_separator: NotRequired[
        "capo_quicksight.types.numeric_separator_symbol.NumericSeparatorSymbol"
    ]
    """<p>Determines the decimal separator.</p>"""
    thousands_separator: NotRequired[
        "capo_quicksight.types.thousand_separator_options.ThousandSeparatorOptions"
    ]
    """<p>The options that determine the thousands separator configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericSeparatorConfiguration) -> dict:
    out: dict = {}
    if "decimal_separator" in value:
        import capo_quicksight.types.numeric_separator_symbol

        out["DecimalSeparator"] = (
            capo_quicksight.types.numeric_separator_symbol.serialize_json(
                value["decimal_separator"]
            )
        )
    if "thousands_separator" in value:
        import capo_quicksight.types.thousand_separator_options

        out["ThousandsSeparator"] = (
            capo_quicksight.types.thousand_separator_options.serialize_json(
                value["thousands_separator"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumericSeparatorConfiguration:
    out: NumericSeparatorConfiguration = {}  # type: ignore[typeddict-item]
    if "DecimalSeparator" in data:
        import capo_quicksight.types.numeric_separator_symbol

        out["decimal_separator"] = (
            capo_quicksight.types.numeric_separator_symbol.deserialize_json(
                data["DecimalSeparator"]
            )
        )
    if "ThousandsSeparator" in data:
        import capo_quicksight.types.thousand_separator_options

        out["thousands_separator"] = (
            capo_quicksight.types.thousand_separator_options.deserialize_json(
                data["ThousandsSeparator"]
            )
        )
    return out
