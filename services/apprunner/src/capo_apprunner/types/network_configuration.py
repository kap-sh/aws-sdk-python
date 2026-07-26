"""Generated from Smithy shape ``com.amazonaws.apprunner#NetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.egress_configuration
    import capo_apprunner.types.ingress_configuration
    import capo_apprunner.types.ip_address_type


class NetworkConfiguration(TypedDict, closed=True):
    egress_configuration: NotRequired[
        "capo_apprunner.types.egress_configuration.EgressConfiguration"
    ]
    """<p>Network configuration settings for outbound message traffic.</p>"""
    ingress_configuration: NotRequired[
        "capo_apprunner.types.ingress_configuration.IngressConfiguration"
    ]
    """<p>Network configuration settings for inbound message traffic.</p>"""
    ip_address_type: NotRequired["capo_apprunner.types.ip_address_type.IpAddressType"]
    """<p>App Runner provides you with the option to choose between <i>IPv4</i> and <i>dual stack</i> (IPv4 and IPv6). This is an optional parameter. If you do not specify an <code>IpAddressType</code>, it defaults to select IPv4.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "egress_configuration" in value:
        import capo_apprunner.types.egress_configuration

        out["EgressConfiguration"] = (
            capo_apprunner.types.egress_configuration.serialize_aws_json_1_0(
                value["egress_configuration"]
            )
        )
    if "ingress_configuration" in value:
        import capo_apprunner.types.ingress_configuration

        out["IngressConfiguration"] = (
            capo_apprunner.types.ingress_configuration.serialize_aws_json_1_0(
                value["ingress_configuration"]
            )
        )
    if "ip_address_type" in value:
        import capo_apprunner.types.ip_address_type

        out["IpAddressType"] = (
            capo_apprunner.types.ip_address_type.serialize_aws_json_1_0(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "EgressConfiguration" in data:
        import capo_apprunner.types.egress_configuration

        out["egress_configuration"] = (
            capo_apprunner.types.egress_configuration.deserialize_aws_json_1_0(
                data["EgressConfiguration"]
            )
        )
    if "IngressConfiguration" in data:
        import capo_apprunner.types.ingress_configuration

        out["ingress_configuration"] = (
            capo_apprunner.types.ingress_configuration.deserialize_aws_json_1_0(
                data["IngressConfiguration"]
            )
        )
    if "IpAddressType" in data:
        import capo_apprunner.types.ip_address_type

        out["ip_address_type"] = (
            capo_apprunner.types.ip_address_type.deserialize_aws_json_1_0(
                data["IpAddressType"]
            )
        )
    return out
