"""Generated from Smithy shape ``com.amazonaws.ec2#DimensionCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.comparison
    import capo_ec2.types.condition_value_list
    import capo_ec2.types.filter_by_dimension


class DimensionCondition(TypedDict, closed=True):
    dimension: NotRequired["capo_ec2.types.filter_by_dimension.FilterByDimension"]
    """<p> The name of the dimension to filter by. </p>"""
    comparison: NotRequired["capo_ec2.types.comparison.Comparison"]
    """<p> The comparison operator to use for the filter. </p>"""
    values: NotRequired["capo_ec2.types.condition_value_list.ConditionValueList"]
    """<p> The list of values to match against the specified dimension. For 'equals' comparison, only the first value is used. For 'in' comparison, any matching value will satisfy the condition. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DimensionCondition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dimension" in value:
        import capo_ec2.types.filter_by_dimension

        capo_ec2.types.filter_by_dimension.serialize_ec2_query(
            value["dimension"], pairs, f"{key_prefix}Dimension"
        )
    if "comparison" in value:
        import capo_ec2.types.comparison

        capo_ec2.types.comparison.serialize_ec2_query(
            value["comparison"], pairs, f"{key_prefix}Comparison"
        )
    if "values" in value:
        import capo_ec2.types.condition_value_list

        capo_ec2.types.condition_value_list.serialize_ec2_query(
            value["values"], pairs, f"{key_prefix}Values"
        )


def deserialize_ec2_query(el: Element) -> DimensionCondition:
    out: DimensionCondition = {}  # type: ignore[typeddict-item]
    child_dimension = el.find("Dimension")
    if child_dimension is not None:
        import capo_ec2.types.filter_by_dimension

        out["dimension"] = capo_ec2.types.filter_by_dimension.deserialize_ec2_query(
            child_dimension
        )
    child_comparison = el.find("Comparison")
    if child_comparison is not None:
        import capo_ec2.types.comparison

        out["comparison"] = capo_ec2.types.comparison.deserialize_ec2_query(
            child_comparison
        )
    if el.find("Values") is not None:
        import capo_ec2.types.condition_value_list

        out["values"] = capo_ec2.types.condition_value_list.deserialize_ec2_query(
            el, "Values"
        )
    return out
