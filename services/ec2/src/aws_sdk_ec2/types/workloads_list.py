"""Generated from Smithy shape ``com.amazonaws.ec2#WorkloadsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.workload

WorkloadsList: TypeAlias = list["aws_sdk_ec2.types.workload.Workload"]
