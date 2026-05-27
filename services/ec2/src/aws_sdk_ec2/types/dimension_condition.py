"""Generated from Smithy shape ``com.amazonaws.ec2#DimensionCondition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.comparison
    import aws_sdk_ec2.types.condition_value_list
    import aws_sdk_ec2.types.filter_by_dimension


class DimensionCondition(TypedDict):
    dimension: NotRequired["aws_sdk_ec2.types.filter_by_dimension.FilterByDimension"]
    """<p> The name of the dimension to filter by. </p>"""
    comparison: NotRequired["aws_sdk_ec2.types.comparison.Comparison"]
    """<p> The comparison operator to use for the filter. </p>"""
    values: NotRequired["aws_sdk_ec2.types.condition_value_list.ConditionValueList"]
    """<p> The list of values to match against the specified dimension. For 'equals' comparison, only the first value is used. For 'in' comparison, any matching value will satisfy the condition. </p>"""
