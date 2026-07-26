"""Generated from Smithy shape ``com.amazonaws.quicksight#DisplayFormatOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.integer
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.negative_format
    import capo_quicksight.types.number_scale
    import capo_quicksight.types.topic_numeric_separator_symbol


class DisplayFormatOptions(TypedDict, closed=True):
    use_blank_cell_format: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether to use blank cell format.</p>"""
    blank_cell_format: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>Determines the blank cell format.</p>"""
    date_format: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>Determines the <code>DateTime</code> format.</p>"""
    decimal_separator: NotRequired[
        "capo_quicksight.types.topic_numeric_separator_symbol.TopicNumericSeparatorSymbol"
    ]
    """<p>Determines the decimal separator.</p>"""
    grouping_separator: NotRequired[
        "capo_quicksight.types.limited_string.LimitedString"
    ]
    """<p>Determines the grouping separator.</p>"""
    use_grouping: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether to use grouping.</p>"""
    fraction_digits: "capo_quicksight.types.integer.Integer"
    """<p>Determines the number of fraction digits.</p>"""
    prefix: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The prefix value for a display format.</p>"""
    suffix: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The suffix value for a display format.</p>"""
    unit_scaler: NotRequired["capo_quicksight.types.number_scale.NumberScale"]
    """<p>The unit scaler. Valid values for this structure are: <code>NONE</code>, <code>AUTO</code>, <code>THOUSANDS</code>, <code>MILLIONS</code>, <code>BILLIONS</code>, and <code>TRILLIONS</code>.</p>"""
    negative_format: NotRequired["capo_quicksight.types.negative_format.NegativeFormat"]
    """<p>The negative format.</p>"""
    currency_symbol: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The currency symbol, such as <code>USD</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisplayFormatOptions) -> dict:
    out: dict = {}
    out["UseBlankCellFormat"] = value.get("use_blank_cell_format", False)
    if "blank_cell_format" in value:
        out["BlankCellFormat"] = value["blank_cell_format"]
    if "date_format" in value:
        out["DateFormat"] = value["date_format"]
    if "decimal_separator" in value:
        import capo_quicksight.types.topic_numeric_separator_symbol

        out["DecimalSeparator"] = (
            capo_quicksight.types.topic_numeric_separator_symbol.serialize_json(
                value["decimal_separator"]
            )
        )
    if "grouping_separator" in value:
        out["GroupingSeparator"] = value["grouping_separator"]
    out["UseGrouping"] = value.get("use_grouping", False)
    out["FractionDigits"] = value.get("fraction_digits", 0)
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "suffix" in value:
        out["Suffix"] = value["suffix"]
    if "unit_scaler" in value:
        import capo_quicksight.types.number_scale

        out["UnitScaler"] = capo_quicksight.types.number_scale.serialize_json(
            value["unit_scaler"]
        )
    if "negative_format" in value:
        import capo_quicksight.types.negative_format

        out["NegativeFormat"] = capo_quicksight.types.negative_format.serialize_json(
            value["negative_format"]
        )
    if "currency_symbol" in value:
        out["CurrencySymbol"] = value["currency_symbol"]
    return out


def deserialize_json(data: dict) -> DisplayFormatOptions:
    out: DisplayFormatOptions = {}  # type: ignore[typeddict-item]
    if "UseBlankCellFormat" in data:
        out["use_blank_cell_format"] = data["UseBlankCellFormat"]
    else:
        out["use_blank_cell_format"] = False
    if "BlankCellFormat" in data:
        out["blank_cell_format"] = data["BlankCellFormat"]
    if "DateFormat" in data:
        out["date_format"] = data["DateFormat"]
    if "DecimalSeparator" in data:
        import capo_quicksight.types.topic_numeric_separator_symbol

        out["decimal_separator"] = (
            capo_quicksight.types.topic_numeric_separator_symbol.deserialize_json(
                data["DecimalSeparator"]
            )
        )
    if "GroupingSeparator" in data:
        out["grouping_separator"] = data["GroupingSeparator"]
    if "UseGrouping" in data:
        out["use_grouping"] = data["UseGrouping"]
    else:
        out["use_grouping"] = False
    if "FractionDigits" in data:
        out["fraction_digits"] = data["FractionDigits"]
    else:
        out["fraction_digits"] = 0
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "Suffix" in data:
        out["suffix"] = data["Suffix"]
    if "UnitScaler" in data:
        import capo_quicksight.types.number_scale

        out["unit_scaler"] = capo_quicksight.types.number_scale.deserialize_json(
            data["UnitScaler"]
        )
    if "NegativeFormat" in data:
        import capo_quicksight.types.negative_format

        out["negative_format"] = capo_quicksight.types.negative_format.deserialize_json(
            data["NegativeFormat"]
        )
    if "CurrencySymbol" in data:
        out["currency_symbol"] = data["CurrencySymbol"]
    return out
