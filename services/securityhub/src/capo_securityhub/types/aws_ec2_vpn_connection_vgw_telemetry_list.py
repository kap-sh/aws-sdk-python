"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpnConnectionVgwTelemetryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_details

AwsEc2VpnConnectionVgwTelemetryList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_details.AwsEc2VpnConnectionVgwTelemetryDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpnConnectionVgwTelemetryList) -> list:
    import capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2VpnConnectionVgwTelemetryList:
    import capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_details

    out: AwsEc2VpnConnectionVgwTelemetryList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_details.deserialize_json(
                item
            )
        )
    return out
