"""Generated from Smithy shape ``com.amazonaws.quicksight#ThousandSeparatorOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.digit_grouping_style
    import aws_sdk_quicksight.types.numeric_separator_symbol
    import aws_sdk_quicksight.types.visibility


class ThousandSeparatorOptions(TypedDict, closed=True):
    symbol: NotRequired[
        "aws_sdk_quicksight.types.numeric_separator_symbol.NumericSeparatorSymbol"
    ]
    """<p>Determines the thousands separator symbol.</p>"""
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines the visibility of the thousands separator.</p>"""
    grouping_style: NotRequired[
        "aws_sdk_quicksight.types.digit_grouping_style.DigitGroupingStyle"
    ]
    """<p>Determines the way numbers are styled to accommodate different readability standards. The <code>DEFAULT</code> value uses the standard international grouping system and groups numbers by the thousands. The <code>LAKHS</code> value uses the Indian numbering system and groups numbers by lakhs and crores.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThousandSeparatorOptions) -> dict:
    out: dict = {}
    if "symbol" in value:
        import aws_sdk_quicksight.types.numeric_separator_symbol

        out["Symbol"] = (
            aws_sdk_quicksight.types.numeric_separator_symbol.serialize_json(
                value["symbol"]
            )
        )
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "grouping_style" in value:
        import aws_sdk_quicksight.types.digit_grouping_style

        out["GroupingStyle"] = (
            aws_sdk_quicksight.types.digit_grouping_style.serialize_json(
                value["grouping_style"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThousandSeparatorOptions:
    out: ThousandSeparatorOptions = {}  # type: ignore[typeddict-item]
    if "Symbol" in data:
        import aws_sdk_quicksight.types.numeric_separator_symbol

        out["symbol"] = (
            aws_sdk_quicksight.types.numeric_separator_symbol.deserialize_json(
                data["Symbol"]
            )
        )
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "GroupingStyle" in data:
        import aws_sdk_quicksight.types.digit_grouping_style

        out["grouping_style"] = (
            aws_sdk_quicksight.types.digit_grouping_style.deserialize_json(
                data["GroupingStyle"]
            )
        )
    return out
