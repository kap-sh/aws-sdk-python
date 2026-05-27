"""Generated from Smithy shape ``com.amazonaws.ec2#Filter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class Filter(TypedDict):
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the filter. Filter names are case-sensitive.</p>"""
    values: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an <code>OR</code>, and the request returns all results that match any of the specified values.</p>"""
