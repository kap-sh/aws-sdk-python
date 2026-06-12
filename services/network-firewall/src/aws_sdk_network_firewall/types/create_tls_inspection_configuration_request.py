"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateTLSInspectionConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.encryption_configuration
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.tag_list
    import aws_sdk_network_firewall.types.tls_inspection_configuration


class CreateTLSInspectionConfigurationRequest(TypedDict):
    tls_inspection_configuration_name: (
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    )
    """<p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p>"""
    tls_inspection_configuration: "aws_sdk_network_firewall.types.tls_inspection_configuration.TLSInspectionConfiguration"
    """<p>The object that defines a TLS inspection configuration. This, along with <a>TLSInspectionConfigurationResponse</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p> <p>Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.</p> <p>To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see <a href=\"https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html\">Inspecting SSL/TLS traffic with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the TLS inspection configuration. </p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTLSInspectionConfigurationRequest) -> dict:
    out: dict = {}
    out["TLSInspectionConfigurationName"] = value["tls_inspection_configuration_name"]
    import aws_sdk_network_firewall.types.tls_inspection_configuration

    out["TLSInspectionConfiguration"] = (
        aws_sdk_network_firewall.types.tls_inspection_configuration.serialize_aws_json_1_0(
            value["tls_inspection_configuration"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "encryption_configuration" in value:
        import aws_sdk_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTLSInspectionConfigurationRequest:
    out: CreateTLSInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "TLSInspectionConfigurationName" in data:
        out["tls_inspection_configuration_name"] = data[
            "TLSInspectionConfigurationName"
        ]
    else:
        raise DeserializationError(
            "CreateTLSInspectionConfigurationRequest.tls_inspection_configuration_name required"
        )
    if "TLSInspectionConfiguration" in data:
        import aws_sdk_network_firewall.types.tls_inspection_configuration

        out["tls_inspection_configuration"] = (
            aws_sdk_network_firewall.types.tls_inspection_configuration.deserialize_aws_json_1_0(
                data["TLSInspectionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTLSInspectionConfigurationRequest.tls_inspection_configuration required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "EncryptionConfiguration" in data:
        import aws_sdk_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    return out
