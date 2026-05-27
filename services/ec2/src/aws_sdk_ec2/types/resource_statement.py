"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceStatement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.value_string_list


class ResourceStatement(TypedDict):
    resources: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The resources.</p>"""
    resource_types: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The resource types.</p>"""
