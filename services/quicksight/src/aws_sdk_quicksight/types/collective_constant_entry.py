"""Generated from Smithy shape ``com.amazonaws.quicksight#CollectiveConstantEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.constant_type
    import aws_sdk_quicksight.types.constant_value_string


class CollectiveConstantEntry(TypedDict, closed=True):
    constant_type: NotRequired["aws_sdk_quicksight.types.constant_type.ConstantType"]
    """<p>The <code>ConstantType</code> of a <code>CollectiveConstantEntry</code>.</p>"""
    value: NotRequired[
        "aws_sdk_quicksight.types.constant_value_string.ConstantValueString"
    ]
    """<p>The value of a <code>CollectiveConstantEntry</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollectiveConstantEntry) -> dict:
    out: dict = {}
    if "constant_type" in value:
        import aws_sdk_quicksight.types.constant_type

        out["ConstantType"] = aws_sdk_quicksight.types.constant_type.serialize_json(
            value["constant_type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CollectiveConstantEntry:
    out: CollectiveConstantEntry = {}  # type: ignore[typeddict-item]
    if "ConstantType" in data:
        import aws_sdk_quicksight.types.constant_type

        out["constant_type"] = aws_sdk_quicksight.types.constant_type.deserialize_json(
            data["ConstantType"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
