"""Generated from Smithy shape ``com.amazonaws.ec2#VgwTelemetryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vgw_telemetry

VgwTelemetryList: TypeAlias = list["aws_sdk_ec2.types.vgw_telemetry.VgwTelemetry"]
