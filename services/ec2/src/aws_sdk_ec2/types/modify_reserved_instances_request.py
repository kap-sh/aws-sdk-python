"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyReservedInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_configuration_list
    import aws_sdk_ec2.types.reserved_instances_id_string_list
    import aws_sdk_ec2.types.string


class ModifyReservedInstancesRequest(TypedDict):
    reserved_instances_ids: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_id_string_list.ReservedInstancesIdStringList"
    ]
    """<p>The IDs of the Reserved Instances to modify.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive token you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    target_configurations: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_configuration_list.ReservedInstancesConfigurationList"
    ]
    """<p>The configuration settings for the Reserved Instances to modify.</p>"""
