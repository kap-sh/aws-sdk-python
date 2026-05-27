"""Generated from Smithy shape ``com.amazonaws.ec2#FlowLogIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_flow_log_id

FlowLogIdList: TypeAlias = list["aws_sdk_ec2.types.vpc_flow_log_id.VpcFlowLogId"]
