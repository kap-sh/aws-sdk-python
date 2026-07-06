"""Generated from Smithy shape ``com.amazonaws.directconnect#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.aws_device
    import aws_sdk_direct_connect.types.aws_device_v2
    import aws_sdk_direct_connect.types.aws_logical_device_id
    import aws_sdk_direct_connect.types.bandwidth
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.connection_name
    import aws_sdk_direct_connect.types.connection_state
    import aws_sdk_direct_connect.types.encryption_mode
    import aws_sdk_direct_connect.types.has_logical_redundancy
    import aws_sdk_direct_connect.types.jumbo_frame_capable
    import aws_sdk_direct_connect.types.lag_id
    import aws_sdk_direct_connect.types.loa_issue_time
    import aws_sdk_direct_connect.types.location_code
    import aws_sdk_direct_connect.types.mac_sec_capable
    import aws_sdk_direct_connect.types.mac_sec_key_list
    import aws_sdk_direct_connect.types.owner_account
    import aws_sdk_direct_connect.types.partner_interconnect_mac_sec_capable
    import aws_sdk_direct_connect.types.partner_name
    import aws_sdk_direct_connect.types.port_encryption_status
    import aws_sdk_direct_connect.types.provider_name
    import aws_sdk_direct_connect.types.region
    import aws_sdk_direct_connect.types.tag_list
    import aws_sdk_direct_connect.types.vlan


class Connection(TypedDict, closed=True):
    owner_account: NotRequired[
        "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The ID of the Amazon Web Services account that owns the connection.</p>"""
    connection_id: NotRequired[
        "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    ]
    """<p>The ID of the connection.</p>"""
    connection_name: NotRequired[
        "aws_sdk_direct_connect.types.connection_name.ConnectionName"
    ]
    """<p>The name of the connection.</p>"""
    connection_state: NotRequired[
        "aws_sdk_direct_connect.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection. The following are the possible values:</p> <ul> <li> <p> <code>ordering</code>: The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.</p> </li> <li> <p> <code>requested</code>: The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.</p> </li> <li> <p> <code>pending</code>: The connection has been approved and is being initialized.</p> </li> <li> <p> <code>available</code>: The network link is up and the connection is ready for use.</p> </li> <li> <p> <code>down</code>: The network link is down.</p> </li> <li> <p> <code>deleting</code>: The connection is being deleted.</p> </li> <li> <p> <code>deleted</code>: The connection has been deleted.</p> </li> <li> <p> <code>rejected</code>: A hosted connection in the <code>ordering</code> state enters the <code>rejected</code> state if it is deleted by the customer.</p> </li> <li> <p> <code>unknown</code>: The state of the connection is not available.</p> </li> </ul>"""
    region: NotRequired["aws_sdk_direct_connect.types.region.Region"]
    """<p>The Amazon Web Services Region where the connection is located.</p>"""
    location: NotRequired["aws_sdk_direct_connect.types.location_code.LocationCode"]
    """<p>The location of the connection.</p>"""
    bandwidth: NotRequired["aws_sdk_direct_connect.types.bandwidth.Bandwidth"]
    """<p>The bandwidth of the connection.</p>"""
    vlan: "aws_sdk_direct_connect.types.vlan.VLAN"
    """<p>The ID of the VLAN.</p>"""
    partner_name: NotRequired["aws_sdk_direct_connect.types.partner_name.PartnerName"]
    """<p>The name of the Direct Connect service provider associated with the connection.</p>"""
    loa_issue_time: NotRequired[
        "aws_sdk_direct_connect.types.loa_issue_time.LoaIssueTime"
    ]
    """<p>The time of the most recent call to <a>DescribeLoa</a> for this connection.</p>"""
    lag_id: NotRequired["aws_sdk_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    aws_device: NotRequired["aws_sdk_direct_connect.types.aws_device.AwsDevice"]
    """<p>The Direct Connect endpoint on which the physical connection terminates.</p>"""
    jumbo_frame_capable: NotRequired[
        "aws_sdk_direct_connect.types.jumbo_frame_capable.JumboFrameCapable"
    ]
    """<p>Indicates whether jumbo frames are supported.</p>"""
    aws_device_v2: NotRequired["aws_sdk_direct_connect.types.aws_device_v2.AwsDeviceV2"]
    """<p>The Direct Connect endpoint that terminates the physical connection.</p>"""
    aws_logical_device_id: NotRequired[
        "aws_sdk_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""
    has_logical_redundancy: NotRequired[
        "aws_sdk_direct_connect.types.has_logical_redundancy.HasLogicalRedundancy"
    ]
    """<p>Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the connection.</p>"""
    provider_name: NotRequired[
        "aws_sdk_direct_connect.types.provider_name.ProviderName"
    ]
    """<p>The name of the service provider associated with the connection.</p>"""
    mac_sec_capable: NotRequired[
        "aws_sdk_direct_connect.types.mac_sec_capable.MacSecCapable"
    ]
    """<p>Indicates whether the connection supports MAC Security (MACsec).</p>"""
    port_encryption_status: NotRequired[
        "aws_sdk_direct_connect.types.port_encryption_status.PortEncryptionStatus"
    ]
    """<p>The MAC Security (MACsec) port link status of the connection.</p> <p>The valid values are <code>Encryption Up</code>, which means that there is an active Connection Key Name, or <code>Encryption Down</code>.</p>"""
    encryption_mode: NotRequired[
        "aws_sdk_direct_connect.types.encryption_mode.EncryptionMode"
    ]
    """<p>The MAC Security (MACsec) connection encryption mode.</p> <p>The valid values are <code>no_encrypt</code>, <code>should_encrypt</code>, and <code>must_encrypt</code>.</p>"""
    mac_sec_keys: NotRequired[
        "aws_sdk_direct_connect.types.mac_sec_key_list.MacSecKeyList"
    ]
    """<p>The MAC Security (MACsec) security keys associated with the connection.</p>"""
    partner_interconnect_mac_sec_capable: NotRequired[
        "aws_sdk_direct_connect.types.partner_interconnect_mac_sec_capable.PartnerInterconnectMacSecCapable"
    ]
    """<p>Indicates whether the interconnect hosting this connection supports MAC Security (MACsec).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connection) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "connection_name" in value:
        out["connectionName"] = value["connection_name"]
    if "connection_state" in value:
        import aws_sdk_direct_connect.types.connection_state

        out["connectionState"] = (
            aws_sdk_direct_connect.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "location" in value:
        out["location"] = value["location"]
    if "bandwidth" in value:
        out["bandwidth"] = value["bandwidth"]
    out["vlan"] = value.get("vlan", 0)
    if "partner_name" in value:
        out["partnerName"] = value["partner_name"]
    if "loa_issue_time" in value:
        import aws_sdk_direct_connect.types.loa_issue_time

        out["loaIssueTime"] = (
            aws_sdk_direct_connect.types.loa_issue_time.serialize_aws_json_1_1(
                value["loa_issue_time"]
            )
        )
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "aws_device" in value:
        out["awsDevice"] = value["aws_device"]
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "has_logical_redundancy" in value:
        import aws_sdk_direct_connect.types.has_logical_redundancy

        out["hasLogicalRedundancy"] = (
            aws_sdk_direct_connect.types.has_logical_redundancy.serialize_aws_json_1_1(
                value["has_logical_redundancy"]
            )
        )
    if "tags" in value:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "mac_sec_capable" in value:
        out["macSecCapable"] = value["mac_sec_capable"]
    if "port_encryption_status" in value:
        out["portEncryptionStatus"] = value["port_encryption_status"]
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    if "mac_sec_keys" in value:
        import aws_sdk_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = (
            aws_sdk_direct_connect.types.mac_sec_key_list.serialize_aws_json_1_1(
                value["mac_sec_keys"]
            )
        )
    if "partner_interconnect_mac_sec_capable" in value:
        out["partnerInterconnectMacSecCapable"] = value[
            "partner_interconnect_mac_sec_capable"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    if "connectionName" in data:
        out["connection_name"] = data["connectionName"]
    if "connectionState" in data:
        import aws_sdk_direct_connect.types.connection_state

        out["connection_state"] = (
            aws_sdk_direct_connect.types.connection_state.deserialize_aws_json_1_1(
                data["connectionState"]
            )
        )
    if "region" in data:
        out["region"] = data["region"]
    if "location" in data:
        out["location"] = data["location"]
    if "bandwidth" in data:
        out["bandwidth"] = data["bandwidth"]
    if "vlan" in data:
        out["vlan"] = data["vlan"]
    else:
        out["vlan"] = 0
    if "partnerName" in data:
        out["partner_name"] = data["partnerName"]
    if "loaIssueTime" in data:
        import aws_sdk_direct_connect.types.loa_issue_time

        out["loa_issue_time"] = (
            aws_sdk_direct_connect.types.loa_issue_time.deserialize_aws_json_1_1(
                data["loaIssueTime"]
            )
        )
    if "lagId" in data:
        out["lag_id"] = data["lagId"]
    if "awsDevice" in data:
        out["aws_device"] = data["awsDevice"]
    if "jumboFrameCapable" in data:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
    if "awsDeviceV2" in data:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if "awsLogicalDeviceId" in data:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if "hasLogicalRedundancy" in data:
        import aws_sdk_direct_connect.types.has_logical_redundancy

        out["has_logical_redundancy"] = (
            aws_sdk_direct_connect.types.has_logical_redundancy.deserialize_aws_json_1_1(
                data["hasLogicalRedundancy"]
            )
        )
    if "tags" in data:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    if "macSecCapable" in data:
        out["mac_sec_capable"] = data["macSecCapable"]
    if "portEncryptionStatus" in data:
        out["port_encryption_status"] = data["portEncryptionStatus"]
    if "encryptionMode" in data:
        out["encryption_mode"] = data["encryptionMode"]
    if "macSecKeys" in data:
        import aws_sdk_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            aws_sdk_direct_connect.types.mac_sec_key_list.deserialize_aws_json_1_1(
                data["macSecKeys"]
            )
        )
    if "partnerInterconnectMacSecCapable" in data:
        out["partner_interconnect_mac_sec_capable"] = data[
            "partnerInterconnectMacSecCapable"
        ]
    return out
