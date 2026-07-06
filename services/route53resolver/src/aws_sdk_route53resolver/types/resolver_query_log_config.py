"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.account_id
    import aws_sdk_route53resolver.types.arn
    import aws_sdk_route53resolver.types.count
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.destination_arn
    import aws_sdk_route53resolver.types.resolver_query_log_config_name
    import aws_sdk_route53resolver.types.resolver_query_log_config_status
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.rfc3339_time_string
    import aws_sdk_route53resolver.types.share_status


class ResolverQueryLogConfig(TypedDict, closed=True):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID for the query logging configuration.</p>"""
    owner_id: NotRequired["aws_sdk_route53resolver.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the account that created the query logging configuration. </p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_status.ResolverQueryLogConfigStatus"
    ]
    """<p>The status of the specified query logging configuration. Valid values include the following:</p> <ul> <li> <p> <code>CREATING</code>: Resolver is creating the query logging configuration.</p> </li> <li> <p> <code>CREATED</code>: The query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.</p> </li> <li> <p> <code>DELETING</code>: Resolver is deleting this query logging configuration.</p> </li> <li> <p> <code>FAILED</code>: Resolver can't deliver logs to the location that is specified in the query logging configuration. Here are two common causes:</p> <ul> <li> <p>The specified destination (for example, an Amazon S3 bucket) was deleted.</p> </li> <li> <p>Permissions don't allow sending logs to the destination.</p> </li> </ul> </li> </ul>"""
    share_status: NotRequired["aws_sdk_route53resolver.types.share_status.ShareStatus"]
    """<p>An indication of whether the query logging configuration is shared with other Amazon Web Services accounts, or was shared with the current account by another Amazon Web Services account. Sharing is configured through Resource Access Manager (RAM).</p>"""
    association_count: "aws_sdk_route53resolver.types.count.Count"
    """<p>The number of VPCs that are associated with the query logging configuration.</p>"""
    arn: NotRequired["aws_sdk_route53resolver.types.arn.Arn"]
    """<p>The ARN for the query logging configuration.</p>"""
    name: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_name.ResolverQueryLogConfigName"
    ]
    """<p>The name of the query logging configuration. </p>"""
    destination_arn: NotRequired[
        "aws_sdk_route53resolver.types.destination_arn.DestinationArn"
    ]
    """<p>The ARN of the resource that you want Resolver to send query logs: an Amazon S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string that identifies the request that created the query logging configuration. The <code>CreatorRequestId</code> allows failed requests to be retried without the risk of running the operation twice.</p>"""
    creation_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the query logging configuration was created, in Unix time format and Coordinated Universal Time (UTC).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverQueryLogConfig) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "status" in value:
        import aws_sdk_route53resolver.types.resolver_query_log_config_status

        out["Status"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "share_status" in value:
        import aws_sdk_route53resolver.types.share_status

        out["ShareStatus"] = (
            aws_sdk_route53resolver.types.share_status.serialize_aws_json_1_1(
                value["share_status"]
            )
        )
    out["AssociationCount"] = value.get("association_count", 0)
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverQueryLogConfig:
    out: ResolverQueryLogConfig = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.resolver_query_log_config_status

        out["status"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ShareStatus" in data:
        import aws_sdk_route53resolver.types.share_status

        out["share_status"] = (
            aws_sdk_route53resolver.types.share_status.deserialize_aws_json_1_1(
                data["ShareStatus"]
            )
        )
    if "AssociationCount" in data:
        out["association_count"] = data["AssociationCount"]
    else:
        out["association_count"] = 0
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    return out
