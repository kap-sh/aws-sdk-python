"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.arn
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.dns64_enabled
    import aws_sdk_route53resolver.types.ip_address_count
    import aws_sdk_route53resolver.types.ipv6_internet_access_enabled
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.outpost_arn
    import aws_sdk_route53resolver.types.outpost_instance_type
    import aws_sdk_route53resolver.types.protocol_list
    import aws_sdk_route53resolver.types.resolver_endpoint_direction
    import aws_sdk_route53resolver.types.resolver_endpoint_status
    import aws_sdk_route53resolver.types.resolver_endpoint_type
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.rfc3339_time_string
    import aws_sdk_route53resolver.types.rni_enhanced_metrics_enabled
    import aws_sdk_route53resolver.types.security_group_ids
    import aws_sdk_route53resolver.types.status_message
    import aws_sdk_route53resolver.types.target_name_server_metrics_enabled


class ResolverEndpoint(TypedDict, closed=True):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the Resolver endpoint.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string that identifies the request that created the Resolver endpoint. The <code>CreatorRequestId</code> allows failed requests to be retried without the risk of running the operation twice.</p>"""
    arn: NotRequired["aws_sdk_route53resolver.types.arn.Arn"]
    """<p>The ARN (Amazon Resource Name) for the Resolver endpoint.</p>"""
    name: NotRequired["aws_sdk_route53resolver.types.name.Name"]
    r"""<p>The name that you assigned to the Resolver endpoint when you submitted a <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html\">CreateResolverEndpoint</a> request.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_route53resolver.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound rules (for inbound endpoints) or outbound rules (for outbound endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.</p>"""
    direction: NotRequired[
        "aws_sdk_route53resolver.types.resolver_endpoint_direction.ResolverEndpointDirection"
    ]
    """<p>Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:</p> <ul> <li> <p> <code>INBOUND</code>: allows DNS queries to your VPC from your network</p> </li> <li> <p> <code>OUTBOUND</code>: allows DNS queries from your VPC to your network</p> </li> <li> <p> <code>INBOUND_DELEGATION</code>: Resolver delegates queries to Route 53 private hosted zones from your network.</p> </li> </ul>"""
    ip_address_count: NotRequired[
        "aws_sdk_route53resolver.types.ip_address_count.IpAddressCount"
    ]
    """<p>The number of IP addresses that the Resolver endpoint can use for DNS queries.</p>"""
    host_vpc_id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the VPC that you want to create the Resolver endpoint in.</p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.resolver_endpoint_status.ResolverEndpointStatus"
    ]
    r"""<p>A code that specifies the current status of the Resolver endpoint. Valid values include the following:</p> <ul> <li> <p> <code>CREATING</code>: Resolver is creating and configuring one or more Amazon VPC network interfaces for this endpoint.</p> </li> <li> <p> <code>OPERATIONAL</code>: The Amazon VPC network interfaces for this endpoint are correctly configured and able to pass inbound or outbound DNS queries between your network and Resolver.</p> </li> <li> <p> <code>UPDATING</code>: Resolver is associating or disassociating one or more network interfaces with this endpoint.</p> </li> <li> <p> <code>AUTO_RECOVERING</code>: Resolver is trying to recover one or more of the network interfaces that are associated with this endpoint. During the recovery process, the endpoint functions with limited capacity because of the limit on the number of DNS queries per IP address (per network interface). For the current limit, see <a href=\"https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-resolver\">Limits on Route 53 Resolver</a>.</p> </li> <li> <p> <code>ACTION_NEEDED</code>: This endpoint is unhealthy, and Resolver can't automatically recover it. To resolve the problem, we recommend that you check each IP address that you associated with the endpoint. For each IP address that isn't available, add another IP address and then delete the IP address that isn't available. (An endpoint must always include at least two IP addresses.) A status of <code>ACTION_NEEDED</code> can have a variety of causes. Here are two common causes:</p> <ul> <li> <p>One or more of the network interfaces that are associated with the endpoint were deleted using Amazon VPC.</p> </li> <li> <p>The network interface couldn't be created for some reason that's outside the control of Resolver.</p> </li> </ul> </li> <li> <p> <code>DELETING</code>: Resolver is deleting this endpoint and the associated network interfaces.</p> </li> </ul>"""
    status_message: NotRequired[
        "aws_sdk_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>A detailed description of the status of the Resolver endpoint.</p>"""
    creation_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    modification_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    outpost_arn: NotRequired["aws_sdk_route53resolver.types.outpost_arn.OutpostArn"]
    """<p>The ARN (Amazon Resource Name) for the Outpost.</p>"""
    preferred_instance_type: NotRequired[
        "aws_sdk_route53resolver.types.outpost_instance_type.OutpostInstanceType"
    ]
    """<p> The Amazon EC2 instance type. </p>"""
    resolver_endpoint_type: NotRequired[
        "aws_sdk_route53resolver.types.resolver_endpoint_type.ResolverEndpointType"
    ]
    """<p> The Resolver endpoint IP address type. </p>"""
    protocols: NotRequired["aws_sdk_route53resolver.types.protocol_list.ProtocolList"]
    """<p> Protocols used for the endpoint. DoH-FIPS is applicable for a default inbound endpoints only. </p> <p>For an inbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 and DoH-FIPS in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>DoH-FIPS alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul> <p>For a delegation inbound endpoint you can use Do53 only.</p> <p>For an outbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul>"""
    rni_enhanced_metrics_enabled: NotRequired[
        "aws_sdk_route53resolver.types.rni_enhanced_metrics_enabled.RniEnhancedMetricsEnabled"
    ]
    """<p>Indicates whether RNI enhanced metrics are enabled for the Resolver endpoint. When enabled, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When disabled, these metrics are not published.</p>"""
    target_name_server_metrics_enabled: NotRequired[
        "aws_sdk_route53resolver.types.target_name_server_metrics_enabled.TargetNameServerMetricsEnabled"
    ]
    """<p>Indicates whether target name server metrics are enabled for the outbound Resolver endpoint. When enabled, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When disabled, these metrics are not published. This feature is not supported for inbound Resolver endpoint.</p>"""
    dns64_enabled: NotRequired[
        "aws_sdk_route53resolver.types.dns64_enabled.Dns64Enabled"
    ]
    """<p>Indicates whether DNS64 is enabled for the inbound Resolver endpoint. When <code>true</code>, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the <code>64:ff9b::/96</code> prefix to the IPv4 address.</p>"""
    ipv6_internet_access_enabled: NotRequired[
        "aws_sdk_route53resolver.types.ipv6_internet_access_enabled.Ipv6InternetAccessEnabled"
    ]
    """<p>Indicates whether IPv6 internet access is enabled for the outbound Resolver endpoint. When <code>true</code>, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverEndpoint) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "security_group_ids" in value:
        import aws_sdk_route53resolver.types.security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_route53resolver.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "direction" in value:
        import aws_sdk_route53resolver.types.resolver_endpoint_direction

        out["Direction"] = (
            aws_sdk_route53resolver.types.resolver_endpoint_direction.serialize_aws_json_1_1(
                value["direction"]
            )
        )
    if "ip_address_count" in value:
        out["IpAddressCount"] = value["ip_address_count"]
    if "host_vpc_id" in value:
        out["HostVPCId"] = value["host_vpc_id"]
    if "status" in value:
        import aws_sdk_route53resolver.types.resolver_endpoint_status

        out["Status"] = (
            aws_sdk_route53resolver.types.resolver_endpoint_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    if "preferred_instance_type" in value:
        out["PreferredInstanceType"] = value["preferred_instance_type"]
    if "resolver_endpoint_type" in value:
        import aws_sdk_route53resolver.types.resolver_endpoint_type

        out["ResolverEndpointType"] = (
            aws_sdk_route53resolver.types.resolver_endpoint_type.serialize_aws_json_1_1(
                value["resolver_endpoint_type"]
            )
        )
    if "protocols" in value:
        import aws_sdk_route53resolver.types.protocol_list

        out["Protocols"] = (
            aws_sdk_route53resolver.types.protocol_list.serialize_aws_json_1_1(
                value["protocols"]
            )
        )
    if "rni_enhanced_metrics_enabled" in value:
        out["RniEnhancedMetricsEnabled"] = value["rni_enhanced_metrics_enabled"]
    if "target_name_server_metrics_enabled" in value:
        out["TargetNameServerMetricsEnabled"] = value[
            "target_name_server_metrics_enabled"
        ]
    if "dns64_enabled" in value:
        out["Dns64Enabled"] = value["dns64_enabled"]
    if "ipv6_internet_access_enabled" in value:
        out["Ipv6InternetAccessEnabled"] = value["ipv6_internet_access_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverEndpoint:
    out: ResolverEndpoint = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SecurityGroupIds" in data:
        import aws_sdk_route53resolver.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_route53resolver.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "Direction" in data:
        import aws_sdk_route53resolver.types.resolver_endpoint_direction

        out["direction"] = (
            aws_sdk_route53resolver.types.resolver_endpoint_direction.deserialize_aws_json_1_1(
                data["Direction"]
            )
        )
    if "IpAddressCount" in data:
        out["ip_address_count"] = data["IpAddressCount"]
    if "HostVPCId" in data:
        out["host_vpc_id"] = data["HostVPCId"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.resolver_endpoint_status

        out["status"] = (
            aws_sdk_route53resolver.types.resolver_endpoint_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "ModificationTime" in data:
        out["modification_time"] = data["ModificationTime"]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    if "PreferredInstanceType" in data:
        out["preferred_instance_type"] = data["PreferredInstanceType"]
    if "ResolverEndpointType" in data:
        import aws_sdk_route53resolver.types.resolver_endpoint_type

        out["resolver_endpoint_type"] = (
            aws_sdk_route53resolver.types.resolver_endpoint_type.deserialize_aws_json_1_1(
                data["ResolverEndpointType"]
            )
        )
    if "Protocols" in data:
        import aws_sdk_route53resolver.types.protocol_list

        out["protocols"] = (
            aws_sdk_route53resolver.types.protocol_list.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    if "RniEnhancedMetricsEnabled" in data:
        out["rni_enhanced_metrics_enabled"] = data["RniEnhancedMetricsEnabled"]
    if "TargetNameServerMetricsEnabled" in data:
        out["target_name_server_metrics_enabled"] = data[
            "TargetNameServerMetricsEnabled"
        ]
    if "Dns64Enabled" in data:
        out["dns64_enabled"] = data["Dns64Enabled"]
    if "Ipv6InternetAccessEnabled" in data:
        out["ipv6_internet_access_enabled"] = data["Ipv6InternetAccessEnabled"]
    return out
