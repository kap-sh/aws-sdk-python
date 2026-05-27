"""Generated from Smithy shape ``com.amazonaws.ec2#ManagedResourceVisibilitySettings``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_resource_default_visibility


class ManagedResourceVisibilitySettings(TypedDict):
    default_visibility: NotRequired[
        "aws_sdk_ec2.types.managed_resource_default_visibility.ManagedResourceDefaultVisibility"
    ]
    """<p>The default visibility setting for managed resources. A value of <code>hidden</code> indicates that managed resources are not included in Describe operation responses by default. A value of <code>visible</code> indicates that managed resources are included by default.</p>"""
