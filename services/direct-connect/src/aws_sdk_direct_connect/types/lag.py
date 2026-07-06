"""Generated from Smithy shape ``com.amazonaws.directconnect#Lag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.aws_device
    import aws_sdk_direct_connect.types.aws_device_v2
    import aws_sdk_direct_connect.types.aws_logical_device_id
    import aws_sdk_direct_connect.types.bandwidth
    import aws_sdk_direct_connect.types.boolean_flag
    import aws_sdk_direct_connect.types.connection_list
    import aws_sdk_direct_connect.types.count
    import aws_sdk_direct_connect.types.encryption_mode
    import aws_sdk_direct_connect.types.has_logical_redundancy
    import aws_sdk_direct_connect.types.jumbo_frame_capable
    import aws_sdk_direct_connect.types.lag_id
    import aws_sdk_direct_connect.types.lag_name
    import aws_sdk_direct_connect.types.lag_state
    import aws_sdk_direct_connect.types.location_code
    import aws_sdk_direct_connect.types.mac_sec_capable
    import aws_sdk_direct_connect.types.mac_sec_key_list
    import aws_sdk_direct_connect.types.owner_account
    import aws_sdk_direct_connect.types.provider_name
    import aws_sdk_direct_connect.types.region
    import aws_sdk_direct_connect.types.tag_list


class Lag(TypedDict, closed=True):
    connections_bandwidth: NotRequired[
        "aws_sdk_direct_connect.types.bandwidth.Bandwidth"
    ]
    """<p>The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps, 10Gbps, 100Gbps, or 400 Gbps.. </p>"""
    number_of_connections: "aws_sdk_direct_connect.types.count.Count"
    """<p>The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1 Gbps or 10 Gbps, or two when the port speed is 100 Gbps or 400 Gbps.</p>"""
    lag_id: NotRequired["aws_sdk_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    owner_account: NotRequired[
        "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The ID of the Amazon Web Services account that owns the LAG.</p>"""
    lag_name: NotRequired["aws_sdk_direct_connect.types.lag_name.LagName"]
    """<p>The name of the LAG.</p>"""
    lag_state: NotRequired["aws_sdk_direct_connect.types.lag_state.LagState"]
    """<p>The state of the LAG. The following are the possible values:</p> <ul> <li> <p> <code>requested</code>: The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.</p> </li> <li> <p> <code>pending</code>: The LAG has been approved and is being initialized.</p> </li> <li> <p> <code>available</code>: The network link is established and the LAG is ready for use.</p> </li> <li> <p> <code>down</code>: The network link is down.</p> </li> <li> <p> <code>deleting</code>: The LAG is being deleted.</p> </li> <li> <p> <code>deleted</code>: The LAG is deleted.</p> </li> <li> <p> <code>unknown</code>: The state of the LAG is not available.</p> </li> </ul>"""
    location: NotRequired["aws_sdk_direct_connect.types.location_code.LocationCode"]
    """<p>The location of the LAG.</p>"""
    region: NotRequired["aws_sdk_direct_connect.types.region.Region"]
    """<p>The Amazon Web Services Region where the connection is located.</p>"""
    minimum_links: "aws_sdk_direct_connect.types.count.Count"
    """<p>The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.</p>"""
    aws_device: NotRequired["aws_sdk_direct_connect.types.aws_device.AwsDevice"]
    """<p>The Direct Connect endpoint that hosts the LAG.</p>"""
    aws_device_v2: NotRequired["aws_sdk_direct_connect.types.aws_device_v2.AwsDeviceV2"]
    """<p>The Direct Connect endpoint that hosts the LAG.</p>"""
    aws_logical_device_id: NotRequired[
        "aws_sdk_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""
    connections: NotRequired[
        "aws_sdk_direct_connect.types.connection_list.ConnectionList"
    ]
    """<p>The connections bundled by the LAG.</p>"""
    allows_hosted_connections: "aws_sdk_direct_connect.types.boolean_flag.BooleanFlag"
    """<p>Indicates whether the LAG can host other connections.</p>"""
    jumbo_frame_capable: NotRequired[
        "aws_sdk_direct_connect.types.jumbo_frame_capable.JumboFrameCapable"
    ]
    """<p>Indicates whether jumbo frames are supported.</p>"""
    has_logical_redundancy: NotRequired[
        "aws_sdk_direct_connect.types.has_logical_redundancy.HasLogicalRedundancy"
    ]
    """<p>Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the LAG.</p>"""
    provider_name: NotRequired[
        "aws_sdk_direct_connect.types.provider_name.ProviderName"
    ]
    """<p>The name of the service provider associated with the LAG.</p>"""
    mac_sec_capable: NotRequired[
        "aws_sdk_direct_connect.types.mac_sec_capable.MacSecCapable"
    ]
    """<p>Indicates whether the LAG supports MAC Security (MACsec).</p>"""
    encryption_mode: NotRequired[
        "aws_sdk_direct_connect.types.encryption_mode.EncryptionMode"
    ]
    """<p>The LAG MAC Security (MACsec) encryption mode.</p> <p>The valid values are <code>no_encrypt</code>, <code>should_encrypt</code>, and <code>must_encrypt</code>.</p>"""
    mac_sec_keys: NotRequired[
        "aws_sdk_direct_connect.types.mac_sec_key_list.MacSecKeyList"
    ]
    """<p>The MAC Security (MACsec) security keys associated with the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Lag) -> dict:
    out: dict = {}
    if "connections_bandwidth" in value:
        out["connectionsBandwidth"] = value["connections_bandwidth"]
    out["numberOfConnections"] = value.get("number_of_connections", 0)
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "lag_name" in value:
        out["lagName"] = value["lag_name"]
    if "lag_state" in value:
        import aws_sdk_direct_connect.types.lag_state

        out["lagState"] = aws_sdk_direct_connect.types.lag_state.serialize_aws_json_1_1(
            value["lag_state"]
        )
    if "location" in value:
        out["location"] = value["location"]
    if "region" in value:
        out["region"] = value["region"]
    out["minimumLinks"] = value.get("minimum_links", 0)
    if "aws_device" in value:
        out["awsDevice"] = value["aws_device"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "connections" in value:
        import aws_sdk_direct_connect.types.connection_list

        out["connections"] = (
            aws_sdk_direct_connect.types.connection_list.serialize_aws_json_1_1(
                value["connections"]
            )
        )
    out["allowsHostedConnections"] = value.get("allows_hosted_connections", False)
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
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
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    if "mac_sec_keys" in value:
        import aws_sdk_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = (
            aws_sdk_direct_connect.types.mac_sec_key_list.serialize_aws_json_1_1(
                value["mac_sec_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Lag:
    out: Lag = {}  # type: ignore[typeddict-item]
    if "connectionsBandwidth" in data:
        out["connections_bandwidth"] = data["connectionsBandwidth"]
    if "numberOfConnections" in data:
        out["number_of_connections"] = data["numberOfConnections"]
    else:
        out["number_of_connections"] = 0
    if "lagId" in data:
        out["lag_id"] = data["lagId"]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "lagName" in data:
        out["lag_name"] = data["lagName"]
    if "lagState" in data:
        import aws_sdk_direct_connect.types.lag_state

        out["lag_state"] = (
            aws_sdk_direct_connect.types.lag_state.deserialize_aws_json_1_1(
                data["lagState"]
            )
        )
    if "location" in data:
        out["location"] = data["location"]
    if "region" in data:
        out["region"] = data["region"]
    if "minimumLinks" in data:
        out["minimum_links"] = data["minimumLinks"]
    else:
        out["minimum_links"] = 0
    if "awsDevice" in data:
        out["aws_device"] = data["awsDevice"]
    if "awsDeviceV2" in data:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if "awsLogicalDeviceId" in data:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if "connections" in data:
        import aws_sdk_direct_connect.types.connection_list

        out["connections"] = (
            aws_sdk_direct_connect.types.connection_list.deserialize_aws_json_1_1(
                data["connections"]
            )
        )
    if "allowsHostedConnections" in data:
        out["allows_hosted_connections"] = data["allowsHostedConnections"]
    else:
        out["allows_hosted_connections"] = False
    if "jumboFrameCapable" in data:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
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
    if "encryptionMode" in data:
        out["encryption_mode"] = data["encryptionMode"]
    if "macSecKeys" in data:
        import aws_sdk_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            aws_sdk_direct_connect.types.mac_sec_key_list.deserialize_aws_json_1_1(
                data["macSecKeys"]
            )
        )
    return out
