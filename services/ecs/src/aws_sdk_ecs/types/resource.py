"""Generated from Smithy shape ``com.amazonaws.ecs#Resource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.double
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.long
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class Resource(TypedDict):
    name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the resource, such as <code>CPU</code>, <code>MEMORY</code>, <code>PORTS</code>, <code>PORTS_UDP</code>, or a user-defined resource.</p>"""
    type: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The type of the resource. Valid values: <code>INTEGER</code>, <code>DOUBLE</code>, <code>LONG</code>, or <code>STRINGSET</code>.</p>"""
    double_value: "aws_sdk_ecs.types.double.Double"
    """<p>When the <code>doubleValue</code> type is set, the value of the resource must be a double precision floating-point type.</p>"""
    long_value: "aws_sdk_ecs.types.long.Long"
    """<p>When the <code>longValue</code> type is set, the value of the resource must be an extended precision floating-point type.</p>"""
    integer_value: "aws_sdk_ecs.types.integer.Integer"
    """<p>When the <code>integerValue</code> type is set, the value of the resource must be an integer.</p>"""
    string_set_value: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>When the <code>stringSetValue</code> type is set, the value of the resource must be a string type.</p>"""
