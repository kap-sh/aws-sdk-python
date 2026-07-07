"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceAccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.host_keys_list
    import aws_sdk_lightsail.types.instance_access_protocol
    import aws_sdk_lightsail.types.ip_address
    import aws_sdk_lightsail.types.ipv6_address_list
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.password_data
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.string


class InstanceAccessDetails(TypedDict, closed=True):
    cert_key: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>For SSH access, the public key to use when accessing your instance For OpenSSH clients (command line SSH), you should save this value to <code>tempkey-cert.pub</code>.</p>"""
    expires_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>For SSH access, the date on which the temporary keys expire.</p>"""
    ip_address: NotRequired["aws_sdk_lightsail.types.ip_address.IpAddress"]
    """<p>The public IP address of the Amazon Lightsail instance.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_lightsail.types.ipv6_address_list.Ipv6AddressList"
    ]
    """<p>The IPv6 address of the Amazon Lightsail instance.</p>"""
    password: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>For RDP access, the password for your Amazon Lightsail instance. Password will be an empty string if the password for your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.</p> <note> <p>If you create an instance using any key pair other than the default (<code>LightsailDefaultKeyPair</code>), <code>password</code> will always be an empty string.</p> <p>If you change the Administrator password on the instance, Lightsail will continue to return the original password value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.</p> </note>"""
    password_data: NotRequired["aws_sdk_lightsail.types.password_data.PasswordData"]
    """<p>For a Windows Server-based instance, an object with the data you can use to retrieve your password. This is only needed if <code>password</code> is empty and the instance is not new (and therefore the password is not ready yet). When you create an instance, it can take up to 15 minutes for the instance to be ready.</p>"""
    private_key: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>For SSH access, the temporary private key. For OpenSSH clients (command line SSH), you should save this value to <code>tempkey</code>).</p>"""
    protocol: NotRequired[
        "aws_sdk_lightsail.types.instance_access_protocol.InstanceAccessProtocol"
    ]
    """<p>The protocol for these Amazon Lightsail instance access details.</p>"""
    instance_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of this Amazon Lightsail instance.</p>"""
    username: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The user name to use when logging in to the Amazon Lightsail instance.</p>"""
    host_keys: NotRequired["aws_sdk_lightsail.types.host_keys_list.HostKeysList"]
    """<p>Describes the public SSH host keys or the RDP certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAccessDetails) -> dict:
    out: dict = {}
    if "cert_key" in value:
        out["certKey"] = value["cert_key"]
    if "expires_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["expiresAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["expires_at"]
        )
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "ipv6_addresses" in value:
        import aws_sdk_lightsail.types.ipv6_address_list

        out["ipv6Addresses"] = (
            aws_sdk_lightsail.types.ipv6_address_list.serialize_aws_json_1_1(
                value["ipv6_addresses"]
            )
        )
    if "password" in value:
        out["password"] = value["password"]
    if "password_data" in value:
        import aws_sdk_lightsail.types.password_data

        out["passwordData"] = (
            aws_sdk_lightsail.types.password_data.serialize_aws_json_1_1(
                value["password_data"]
            )
        )
    if "private_key" in value:
        out["privateKey"] = value["private_key"]
    if "protocol" in value:
        import aws_sdk_lightsail.types.instance_access_protocol

        out["protocol"] = (
            aws_sdk_lightsail.types.instance_access_protocol.serialize_aws_json_1_1(
                value["protocol"]
            )
        )
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "username" in value:
        out["username"] = value["username"]
    if "host_keys" in value:
        import aws_sdk_lightsail.types.host_keys_list

        out["hostKeys"] = aws_sdk_lightsail.types.host_keys_list.serialize_aws_json_1_1(
            value["host_keys"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAccessDetails:
    out: InstanceAccessDetails = {}  # type: ignore[typeddict-item]
    if "certKey" in data:
        out["cert_key"] = data["certKey"]
    if "expiresAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["expires_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["expiresAt"]
        )
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "ipv6Addresses" in data:
        import aws_sdk_lightsail.types.ipv6_address_list

        out["ipv6_addresses"] = (
            aws_sdk_lightsail.types.ipv6_address_list.deserialize_aws_json_1_1(
                data["ipv6Addresses"]
            )
        )
    if "password" in data:
        out["password"] = data["password"]
    if "passwordData" in data:
        import aws_sdk_lightsail.types.password_data

        out["password_data"] = (
            aws_sdk_lightsail.types.password_data.deserialize_aws_json_1_1(
                data["passwordData"]
            )
        )
    if "privateKey" in data:
        out["private_key"] = data["privateKey"]
    if "protocol" in data:
        import aws_sdk_lightsail.types.instance_access_protocol

        out["protocol"] = (
            aws_sdk_lightsail.types.instance_access_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    if "username" in data:
        out["username"] = data["username"]
    if "hostKeys" in data:
        import aws_sdk_lightsail.types.host_keys_list

        out["host_keys"] = (
            aws_sdk_lightsail.types.host_keys_list.deserialize_aws_json_1_1(
                data["hostKeys"]
            )
        )
    return out
