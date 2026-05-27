"""Generated from Smithy shape ``com.amazonaws.ecs#Attribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.target_type


class Attribute(TypedDict):
    name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the attribute. The <code>name</code> must contain between 1 and 128 characters. The name may contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), forward slashes (/), back slashes (\), or periods (.).</p>"""
    value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The value of the attribute. The <code>value</code> must contain between 1 and 128 characters. It can contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), periods (.), at signs (@), forward slashes (/), back slashes (\), colons (:), or spaces. The value can't start or end with a space.</p>"""
    target_type: NotRequired["aws_sdk_ecs.types.target_type.TargetType"]
    """<p>The type of the target to attach the attribute with. This parameter is required if you use the short form ID for a resource instead of the full ARN.</p>"""
    target_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).</p>"""
