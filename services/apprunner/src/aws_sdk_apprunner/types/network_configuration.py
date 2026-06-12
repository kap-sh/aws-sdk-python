"""Generated from Smithy shape ``com.amazonaws.apprunner#NetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.egress_configuration
    import aws_sdk_apprunner.types.ingress_configuration
    import aws_sdk_apprunner.types.ip_address_type


class NetworkConfiguration(TypedDict):
    egress_configuration: NotRequired[
        "aws_sdk_apprunner.types.egress_configuration.EgressConfiguration"
    ]
    """<p>Network configuration settings for outbound message traffic.</p>"""
    ingress_configuration: NotRequired[
        "aws_sdk_apprunner.types.ingress_configuration.IngressConfiguration"
    ]
    """<p>Network configuration settings for inbound message traffic.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_apprunner.types.ip_address_type.IpAddressType"
    ]
    """<p>App Runner provides you with the option to choose between <i>IPv4</i> and <i>dual stack</i> (IPv4 and IPv6). This is an optional parameter. If you do not specify an <code>IpAddressType</code>, it defaults to select IPv4.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "egress_configuration" in value:
        import aws_sdk_apprunner.types.egress_configuration

        out["EgressConfiguration"] = (
            aws_sdk_apprunner.types.egress_configuration.serialize_aws_json_1_0(
                value["egress_configuration"]
            )
        )
    if "ingress_configuration" in value:
        import aws_sdk_apprunner.types.ingress_configuration

        out["IngressConfiguration"] = (
            aws_sdk_apprunner.types.ingress_configuration.serialize_aws_json_1_0(
                value["ingress_configuration"]
            )
        )
    if "ip_address_type" in value:
        import aws_sdk_apprunner.types.ip_address_type

        out["IpAddressType"] = (
            aws_sdk_apprunner.types.ip_address_type.serialize_aws_json_1_0(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "EgressConfiguration" in data:
        import aws_sdk_apprunner.types.egress_configuration

        out["egress_configuration"] = (
            aws_sdk_apprunner.types.egress_configuration.deserialize_aws_json_1_0(
                data["EgressConfiguration"]
            )
        )
    if "IngressConfiguration" in data:
        import aws_sdk_apprunner.types.ingress_configuration

        out["ingress_configuration"] = (
            aws_sdk_apprunner.types.ingress_configuration.deserialize_aws_json_1_0(
                data["IngressConfiguration"]
            )
        )
    if "IpAddressType" in data:
        import aws_sdk_apprunner.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_apprunner.types.ip_address_type.deserialize_aws_json_1_0(
                data["IpAddressType"]
            )
        )
    return out
