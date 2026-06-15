"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeTLSInspectionConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.tls_inspection_configuration
    import aws_sdk_network_firewall.types.tls_inspection_configuration_response
    import aws_sdk_network_firewall.types.update_token


class DescribeTLSInspectionConfigurationResponse(TypedDict):
    update_token: "aws_sdk_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the TLS inspection configuration. The token marks the state of the TLS inspection configuration resource at the time of the request. </p> <p>To make changes to the TLS inspection configuration, you provide the token in your request. Network Firewall uses the token to ensure that the TLS inspection configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the TLS inspection configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    tls_inspection_configuration: NotRequired[
        "aws_sdk_network_firewall.types.tls_inspection_configuration.TLSInspectionConfiguration"
    ]
    r"""<p>The object that defines a TLS inspection configuration. This, along with <a>TLSInspectionConfigurationResponse</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p> <p>Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.</p> <p>To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see <a href=\"https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html\">Inspecting SSL/TLS traffic with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    tls_inspection_configuration_response: "aws_sdk_network_firewall.types.tls_inspection_configuration_response.TLSInspectionConfigurationResponse"
    """<p>The high-level properties of a TLS inspection configuration. This, along with the <a>TLSInspectionConfiguration</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeTLSInspectionConfigurationResponse) -> dict:
    out: dict = {}
    out["UpdateToken"] = value["update_token"]
    if "tls_inspection_configuration" in value:
        import aws_sdk_network_firewall.types.tls_inspection_configuration

        out["TLSInspectionConfiguration"] = (
            aws_sdk_network_firewall.types.tls_inspection_configuration.serialize_aws_json_1_0(
                value["tls_inspection_configuration"]
            )
        )
    import aws_sdk_network_firewall.types.tls_inspection_configuration_response

    out["TLSInspectionConfigurationResponse"] = (
        aws_sdk_network_firewall.types.tls_inspection_configuration_response.serialize_aws_json_1_0(
            value["tls_inspection_configuration_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeTLSInspectionConfigurationResponse:
    out: DescribeTLSInspectionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    else:
        raise DeserializationError(
            "DescribeTLSInspectionConfigurationResponse.update_token required"
        )
    if "TLSInspectionConfiguration" in data:
        import aws_sdk_network_firewall.types.tls_inspection_configuration

        out["tls_inspection_configuration"] = (
            aws_sdk_network_firewall.types.tls_inspection_configuration.deserialize_aws_json_1_0(
                data["TLSInspectionConfiguration"]
            )
        )
    if "TLSInspectionConfigurationResponse" in data:
        import aws_sdk_network_firewall.types.tls_inspection_configuration_response

        out["tls_inspection_configuration_response"] = (
            aws_sdk_network_firewall.types.tls_inspection_configuration_response.deserialize_aws_json_1_0(
                data["TLSInspectionConfigurationResponse"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeTLSInspectionConfigurationResponse.tls_inspection_configuration_response required"
        )
    return out
