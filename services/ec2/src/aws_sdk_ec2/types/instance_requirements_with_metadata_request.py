"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceRequirementsWithMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_type_set
    import aws_sdk_ec2.types.instance_requirements_request
    import aws_sdk_ec2.types.virtualization_type_set


class InstanceRequirementsWithMetadataRequest(TypedDict):
    architecture_types: NotRequired[
        "aws_sdk_ec2.types.architecture_type_set.ArchitectureTypeSet"
    ]
    """<p>The architecture type.</p>"""
    virtualization_types: NotRequired[
        "aws_sdk_ec2.types.virtualization_type_set.VirtualizationTypeSet"
    ]
    """<p>The virtualization type.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p>"""
