"""Generated from Smithy shape ``com.amazonaws.ec2#FlowLogSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.flow_log

FlowLogSet: TypeAlias = list["aws_sdk_ec2.types.flow_log.FlowLog"]
