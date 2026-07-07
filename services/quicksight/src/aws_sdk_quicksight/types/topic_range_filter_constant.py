"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRangeFilterConstant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.constant_type
    import aws_sdk_quicksight.types.range_constant


class TopicRangeFilterConstant(TypedDict, closed=True):
    constant_type: NotRequired["aws_sdk_quicksight.types.constant_type.ConstantType"]
    """<p>The data type of the constant value that is used in a range filter. Valid values for this structure are <code>RANGE</code>.</p>"""
    range_constant: NotRequired["aws_sdk_quicksight.types.range_constant.RangeConstant"]
    """<p>The value of the constant that is used to specify the endpoints of a range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRangeFilterConstant) -> dict:
    out: dict = {}
    if "constant_type" in value:
        import aws_sdk_quicksight.types.constant_type

        out["ConstantType"] = aws_sdk_quicksight.types.constant_type.serialize_json(
            value["constant_type"]
        )
    if "range_constant" in value:
        import aws_sdk_quicksight.types.range_constant

        out["RangeConstant"] = aws_sdk_quicksight.types.range_constant.serialize_json(
            value["range_constant"]
        )
    return out


def deserialize_json(data: dict) -> TopicRangeFilterConstant:
    out: TopicRangeFilterConstant = {}  # type: ignore[typeddict-item]
    if "ConstantType" in data:
        import aws_sdk_quicksight.types.constant_type

        out["constant_type"] = aws_sdk_quicksight.types.constant_type.deserialize_json(
            data["ConstantType"]
        )
    if "RangeConstant" in data:
        import aws_sdk_quicksight.types.range_constant

        out["range_constant"] = (
            aws_sdk_quicksight.types.range_constant.deserialize_json(
                data["RangeConstant"]
            )
        )
    return out
