"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSingularFilterConstant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.constant_type
    import aws_sdk_quicksight.types.limited_string


class TopicSingularFilterConstant(TypedDict, closed=True):
    constant_type: NotRequired["aws_sdk_quicksight.types.constant_type.ConstantType"]
    """<p>The type of the singular filter constant. Valid values for this structure are <code>SINGULAR</code>.</p>"""
    singular_constant: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>The value of the singular filter constant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicSingularFilterConstant) -> dict:
    out: dict = {}
    if "constant_type" in value:
        import aws_sdk_quicksight.types.constant_type

        out["ConstantType"] = aws_sdk_quicksight.types.constant_type.serialize_json(
            value["constant_type"]
        )
    if "singular_constant" in value:
        out["SingularConstant"] = value["singular_constant"]
    return out


def deserialize_json(data: dict) -> TopicSingularFilterConstant:
    out: TopicSingularFilterConstant = {}  # type: ignore[typeddict-item]
    if "ConstantType" in data:
        import aws_sdk_quicksight.types.constant_type

        out["constant_type"] = aws_sdk_quicksight.types.constant_type.deserialize_json(
            data["ConstantType"]
        )
    if "SingularConstant" in data:
        out["singular_constant"] = data["SingularConstant"]
    return out
