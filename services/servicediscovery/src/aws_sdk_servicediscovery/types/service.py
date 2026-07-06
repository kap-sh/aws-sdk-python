"""Generated from Smithy shape ``com.amazonaws.servicediscovery#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.arn
    import aws_sdk_servicediscovery.types.aws_account_id
    import aws_sdk_servicediscovery.types.dns_config
    import aws_sdk_servicediscovery.types.health_check_config
    import aws_sdk_servicediscovery.types.health_check_custom_config
    import aws_sdk_servicediscovery.types.resource_count
    import aws_sdk_servicediscovery.types.resource_description
    import aws_sdk_servicediscovery.types.resource_id
    import aws_sdk_servicediscovery.types.service_name
    import aws_sdk_servicediscovery.types.service_type
    import aws_sdk_servicediscovery.types.timestamp


class Service(TypedDict, closed=True):
    id: NotRequired["aws_sdk_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID that Cloud Map assigned to the service when you created it.</p>"""
    arn: NotRequired["aws_sdk_servicediscovery.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that Cloud Map assigns to the service when you create it.</p>"""
    resource_owner: NotRequired[
        "aws_sdk_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    r"""<p>The ID of the Amazon Web Services account that created the namespace with which the service is associated. If this isn't your account ID, it is the ID of the account that shared the namespace with your account. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    name: NotRequired["aws_sdk_servicediscovery.types.service_name.ServiceName"]
    """<p>The name of the service.</p>"""
    namespace_id: NotRequired["aws_sdk_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID of the namespace that was used to create the service.</p>"""
    description: NotRequired[
        "aws_sdk_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the service.</p>"""
    instance_count: NotRequired[
        "aws_sdk_servicediscovery.types.resource_count.ResourceCount"
    ]
    """<p>The number of instances that are currently associated with the service. Instances that were previously associated with the service but that are deleted aren't included in the count. The count might not reflect pending registrations and deregistrations.</p>"""
    dns_config: NotRequired["aws_sdk_servicediscovery.types.dns_config.DnsConfig"]
    """<p>A complex type that contains information about the Route 53 DNS records that you want Cloud Map to create when you register an instance.</p> <important> <p>The record types of a service can only be changed by deleting the service and recreating it with a new <code>Dnsconfig</code>.</p> </important>"""
    type: NotRequired["aws_sdk_servicediscovery.types.service_type.ServiceType"]
    """<p>Describes the systems that can be used to discover the service instances.</p> <dl> <dt>DNS_HTTP</dt> <dd> <p>The service instances can be discovered using either DNS queries or the <code>DiscoverInstances</code> API operation.</p> </dd> <dt>HTTP</dt> <dd> <p>The service instances can only be discovered using the <code>DiscoverInstances</code> API operation.</p> </dd> <dt>DNS</dt> <dd> <p>Reserved.</p> </dd> </dl>"""
    health_check_config: NotRequired[
        "aws_sdk_servicediscovery.types.health_check_config.HealthCheckConfig"
    ]
    r"""<p> <i>Public DNS and HTTP namespaces only.</i> A complex type that contains settings for an optional health check. If you specify settings for a health check, Cloud Map associates the health check with the records that you specify in <code>DnsConfig</code>.</p> <p>For information about the charges for health checks, see <a href=\"http://aws.amazon.com/route53/pricing/\">Amazon Route 53 Pricing</a>.</p>"""
    health_check_custom_config: NotRequired[
        "aws_sdk_servicediscovery.types.health_check_custom_config.HealthCheckCustomConfig"
    ]
    """<p>A complex type that contains information about an optional custom health check.</p> <important> <p>If you specify a health check configuration, you can specify either <code>HealthCheckCustomConfig</code> or <code>HealthCheckConfig</code> but not both.</p> </important>"""
    create_date: NotRequired["aws_sdk_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date and time that the service was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreateDate</code> is accurate to milliseconds. For example, the value <code>1516925490.087</code> represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/timestamp).</p>"""
    created_by_account: NotRequired[
        "aws_sdk_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    r"""<p>The ID of the Amazon Web Services account that created the service. If this isn't your account ID, it is the ID of account of the namespace owner or of another account with which the namespace has been shared. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Service) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "name" in value:
        out["Name"] = value["name"]
    if "namespace_id" in value:
        out["NamespaceId"] = value["namespace_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "dns_config" in value:
        import aws_sdk_servicediscovery.types.dns_config

        out["DnsConfig"] = (
            aws_sdk_servicediscovery.types.dns_config.serialize_aws_json_1_1(
                value["dns_config"]
            )
        )
    if "type" in value:
        import aws_sdk_servicediscovery.types.service_type

        out["Type"] = (
            aws_sdk_servicediscovery.types.service_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "health_check_config" in value:
        import aws_sdk_servicediscovery.types.health_check_config

        out["HealthCheckConfig"] = (
            aws_sdk_servicediscovery.types.health_check_config.serialize_aws_json_1_1(
                value["health_check_config"]
            )
        )
    if "health_check_custom_config" in value:
        import aws_sdk_servicediscovery.types.health_check_custom_config

        out["HealthCheckCustomConfig"] = (
            aws_sdk_servicediscovery.types.health_check_custom_config.serialize_aws_json_1_1(
                value["health_check_custom_config"]
            )
        )
    if "create_date" in value:
        import aws_sdk_servicediscovery.types.timestamp

        out["CreateDate"] = (
            aws_sdk_servicediscovery.types.timestamp.serialize_aws_json_1_1(
                value["create_date"]
            )
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "created_by_account" in value:
        out["CreatedByAccount"] = value["created_by_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ResourceOwner" in data:
        out["resource_owner"] = data["ResourceOwner"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "NamespaceId" in data:
        out["namespace_id"] = data["NamespaceId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "DnsConfig" in data:
        import aws_sdk_servicediscovery.types.dns_config

        out["dns_config"] = (
            aws_sdk_servicediscovery.types.dns_config.deserialize_aws_json_1_1(
                data["DnsConfig"]
            )
        )
    if "Type" in data:
        import aws_sdk_servicediscovery.types.service_type

        out["type"] = (
            aws_sdk_servicediscovery.types.service_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "HealthCheckConfig" in data:
        import aws_sdk_servicediscovery.types.health_check_config

        out["health_check_config"] = (
            aws_sdk_servicediscovery.types.health_check_config.deserialize_aws_json_1_1(
                data["HealthCheckConfig"]
            )
        )
    if "HealthCheckCustomConfig" in data:
        import aws_sdk_servicediscovery.types.health_check_custom_config

        out["health_check_custom_config"] = (
            aws_sdk_servicediscovery.types.health_check_custom_config.deserialize_aws_json_1_1(
                data["HealthCheckCustomConfig"]
            )
        )
    if "CreateDate" in data:
        import aws_sdk_servicediscovery.types.timestamp

        out["create_date"] = (
            aws_sdk_servicediscovery.types.timestamp.deserialize_aws_json_1_1(
                data["CreateDate"]
            )
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "CreatedByAccount" in data:
        out["created_by_account"] = data["CreatedByAccount"]
    return out
