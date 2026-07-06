"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicConstantValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.collective_constant_entry_list
    import aws_sdk_quicksight.types.constant_type
    import aws_sdk_quicksight.types.constant_value_string


class TopicConstantValue(TypedDict, closed=True):
    constant_type: NotRequired["aws_sdk_quicksight.types.constant_type.ConstantType"]
    """<p>The constant type of a <code>TopicConstantValue</code>.</p>"""
    value: NotRequired[
        "aws_sdk_quicksight.types.constant_value_string.ConstantValueString"
    ]
    """<p>The value of the <code>TopicConstantValue</code>.</p>"""
    minimum: NotRequired[
        "aws_sdk_quicksight.types.constant_value_string.ConstantValueString"
    ]
    """<p>The minimum for the <code>TopicConstantValue</code>.</p>"""
    maximum: NotRequired[
        "aws_sdk_quicksight.types.constant_value_string.ConstantValueString"
    ]
    """<p>The maximum for the <code>TopicConstantValue</code>.</p>"""
    value_list: NotRequired[
        "aws_sdk_quicksight.types.collective_constant_entry_list.CollectiveConstantEntryList"
    ]
    """<p>The value list of the <code>TopicConstantValue</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicConstantValue) -> dict:
    out: dict = {}
    if "constant_type" in value:
        import aws_sdk_quicksight.types.constant_type

        out["ConstantType"] = aws_sdk_quicksight.types.constant_type.serialize_json(
            value["constant_type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    if "value_list" in value:
        import aws_sdk_quicksight.types.collective_constant_entry_list

        out["ValueList"] = (
            aws_sdk_quicksight.types.collective_constant_entry_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicConstantValue:
    out: TopicConstantValue = {}  # type: ignore[typeddict-item]
    if "ConstantType" in data:
        import aws_sdk_quicksight.types.constant_type

        out["constant_type"] = aws_sdk_quicksight.types.constant_type.deserialize_json(
            data["ConstantType"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    if "ValueList" in data:
        import aws_sdk_quicksight.types.collective_constant_entry_list

        out["value_list"] = (
            aws_sdk_quicksight.types.collective_constant_entry_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
