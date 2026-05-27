"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTypesFromInstanceRequirementsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_info_from_instance_requirements_set
    import aws_sdk_ec2.types.string


class GetInstanceTypesFromInstanceRequirementsResult(TypedDict):
    instance_types: NotRequired[
        "aws_sdk_ec2.types.instance_type_info_from_instance_requirements_set.InstanceTypeInfoFromInstanceRequirementsSet"
    ]
    """<p>The instance types with the specified instance attributes.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
