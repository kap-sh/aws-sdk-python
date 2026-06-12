"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedSecurityPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.fips
    import aws_sdk_transfer.types.security_policy_name
    import aws_sdk_transfer.types.security_policy_options
    import aws_sdk_transfer.types.security_policy_protocols
    import aws_sdk_transfer.types.security_policy_resource_type


class DescribedSecurityPolicy(TypedDict):
    fips: NotRequired["aws_sdk_transfer.types.fips.Fips"]
    """<p>Specifies whether this policy enables Federal Information Processing Standards (FIPS). This parameter applies to both server and connector security policies.</p>"""
    security_policy_name: (
        "aws_sdk_transfer.types.security_policy_name.SecurityPolicyName"
    )
    """<p>The text name of the specified security policy.</p>"""
    ssh_ciphers: NotRequired[
        "aws_sdk_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the enabled Secure Shell (SSH) cipher encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.</p>"""
    ssh_kexs: NotRequired[
        "aws_sdk_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the enabled SSH key exchange (KEX) encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.</p>"""
    ssh_macs: NotRequired[
        "aws_sdk_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the enabled SSH message authentication code (MAC) encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.</p>"""
    tls_ciphers: NotRequired[
        "aws_sdk_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the enabled Transport Layer Security (TLS) cipher encryption algorithms in the security policy that is attached to the server.</p> <note> <p>This parameter only applies to security policies for servers.</p> </note>"""
    ssh_host_key_algorithms: NotRequired[
        "aws_sdk_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the host key algorithms for the security policy.</p> <note> <p>This parameter only applies to security policies for connectors.</p> </note>"""
    type: NotRequired[
        "aws_sdk_transfer.types.security_policy_resource_type.SecurityPolicyResourceType"
    ]
    """<p>The resource type to which the security policy applies, either server or connector.</p>"""
    protocols: NotRequired[
        "aws_sdk_transfer.types.security_policy_protocols.SecurityPolicyProtocols"
    ]
    """<p>Lists the file transfer protocols that the security policy applies to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedSecurityPolicy) -> dict:
    out: dict = {}
    if "fips" in value:
        out["Fips"] = value["fips"]
    out["SecurityPolicyName"] = value["security_policy_name"]
    if "ssh_ciphers" in value:
        import aws_sdk_transfer.types.security_policy_options

        out["SshCiphers"] = (
            aws_sdk_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["ssh_ciphers"]
            )
        )
    if "ssh_kexs" in value:
        import aws_sdk_transfer.types.security_policy_options

        out["SshKexs"] = (
            aws_sdk_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["ssh_kexs"]
            )
        )
    if "ssh_macs" in value:
        import aws_sdk_transfer.types.security_policy_options

        out["SshMacs"] = (
            aws_sdk_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["ssh_macs"]
            )
        )
    if "tls_ciphers" in value:
        import aws_sdk_transfer.types.security_policy_options

        out["TlsCiphers"] = (
            aws_sdk_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["tls_ciphers"]
            )
        )
    if "ssh_host_key_algorithms" in value:
        import aws_sdk_transfer.types.security_policy_options

        out["SshHostKeyAlgorithms"] = (
            aws_sdk_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["ssh_host_key_algorithms"]
            )
        )
    if "type" in value:
        import aws_sdk_transfer.types.security_policy_resource_type

        out["Type"] = (
            aws_sdk_transfer.types.security_policy_resource_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "protocols" in value:
        import aws_sdk_transfer.types.security_policy_protocols

        out["Protocols"] = (
            aws_sdk_transfer.types.security_policy_protocols.serialize_aws_json_1_1(
                value["protocols"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedSecurityPolicy:
    out: DescribedSecurityPolicy = {}  # type: ignore[typeddict-item]
    if "Fips" in data:
        out["fips"] = data["Fips"]
    if "SecurityPolicyName" in data:
        out["security_policy_name"] = data["SecurityPolicyName"]
    else:
        raise DeserializationError(
            "DescribedSecurityPolicy.security_policy_name required"
        )
    if "SshCiphers" in data:
        import aws_sdk_transfer.types.security_policy_options

        out["ssh_ciphers"] = (
            aws_sdk_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["SshCiphers"]
            )
        )
    if "SshKexs" in data:
        import aws_sdk_transfer.types.security_policy_options

        out["ssh_kexs"] = (
            aws_sdk_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["SshKexs"]
            )
        )
    if "SshMacs" in data:
        import aws_sdk_transfer.types.security_policy_options

        out["ssh_macs"] = (
            aws_sdk_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["SshMacs"]
            )
        )
    if "TlsCiphers" in data:
        import aws_sdk_transfer.types.security_policy_options

        out["tls_ciphers"] = (
            aws_sdk_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["TlsCiphers"]
            )
        )
    if "SshHostKeyAlgorithms" in data:
        import aws_sdk_transfer.types.security_policy_options

        out["ssh_host_key_algorithms"] = (
            aws_sdk_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["SshHostKeyAlgorithms"]
            )
        )
    if "Type" in data:
        import aws_sdk_transfer.types.security_policy_resource_type

        out["type"] = (
            aws_sdk_transfer.types.security_policy_resource_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Protocols" in data:
        import aws_sdk_transfer.types.security_policy_protocols

        out["protocols"] = (
            aws_sdk_transfer.types.security_policy_protocols.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    return out
