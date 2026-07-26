"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicCategoryFilterConstant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.collective_constant
    import capo_quicksight.types.constant_type
    import capo_quicksight.types.limited_string


class TopicCategoryFilterConstant(TypedDict, closed=True):
    constant_type: NotRequired["capo_quicksight.types.constant_type.ConstantType"]
    """<p>The type of category filter constant. This element is used to specify whether a constant is a singular or collective. Valid values are <code>SINGULAR</code> and <code>COLLECTIVE</code>.</p>"""
    singular_constant: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>A singular constant used in a category filter. This element is used to specify a single value for the constant.</p>"""
    collective_constant: NotRequired[
        "capo_quicksight.types.collective_constant.CollectiveConstant"
    ]
    """<p>A collective constant used in a category filter. This element is used to specify a list of values for the constant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicCategoryFilterConstant) -> dict:
    out: dict = {}
    if "constant_type" in value:
        import capo_quicksight.types.constant_type

        out["ConstantType"] = capo_quicksight.types.constant_type.serialize_json(
            value["constant_type"]
        )
    if "singular_constant" in value:
        out["SingularConstant"] = value["singular_constant"]
    if "collective_constant" in value:
        import capo_quicksight.types.collective_constant

        out["CollectiveConstant"] = (
            capo_quicksight.types.collective_constant.serialize_json(
                value["collective_constant"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicCategoryFilterConstant:
    out: TopicCategoryFilterConstant = {}  # type: ignore[typeddict-item]
    if "ConstantType" in data:
        import capo_quicksight.types.constant_type

        out["constant_type"] = capo_quicksight.types.constant_type.deserialize_json(
            data["ConstantType"]
        )
    if "SingularConstant" in data:
        out["singular_constant"] = data["SingularConstant"]
    if "CollectiveConstant" in data:
        import capo_quicksight.types.collective_constant

        out["collective_constant"] = (
            capo_quicksight.types.collective_constant.deserialize_json(
                data["CollectiveConstant"]
            )
        )
    return out
