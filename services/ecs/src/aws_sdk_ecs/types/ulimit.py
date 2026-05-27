"""Generated from Smithy shape ``com.amazonaws.ecs#Ulimit``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.ulimit_name


class Ulimit(TypedDict):
    name: "aws_sdk_ecs.types.ulimit_name.UlimitName"
    """<p>The <code>type</code> of the <code>ulimit</code>.</p>"""
    soft_limit: "aws_sdk_ecs.types.integer.Integer"
    """<p>The soft limit for the <code>ulimit</code> type. The value can be specified in bytes, seconds, or as a count, depending on the <code>type</code> of the <code>ulimit</code>.</p>"""
    hard_limit: "aws_sdk_ecs.types.integer.Integer"
    """<p>The hard limit for the <code>ulimit</code> type. The value can be specified in bytes, seconds, or as a count, depending on the <code>type</code> of the <code>ulimit</code>.</p>"""
