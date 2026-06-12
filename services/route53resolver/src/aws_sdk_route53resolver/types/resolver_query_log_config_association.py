"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_query_log_config_association_error
    import aws_sdk_route53resolver.types.resolver_query_log_config_association_error_message
    import aws_sdk_route53resolver.types.resolver_query_log_config_association_status
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.rfc3339_time_string


class ResolverQueryLogConfigAssociation(TypedDict):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the query logging association.</p>"""
    resolver_query_log_config_id: NotRequired[
        "aws_sdk_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the query logging configuration that a VPC is associated with.</p>"""
    resource_id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the Amazon VPC that is associated with the query logging configuration.</p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_association_status.ResolverQueryLogConfigAssociationStatus"
    ]
    """<p>The status of the specified query logging association. Valid values include the following:</p> <ul> <li> <p> <code>CREATING</code>: Resolver is creating an association between an Amazon VPC and a query logging configuration.</p> </li> <li> <p> <code>ACTIVE</code>: The association between an Amazon VPC and a query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.</p> </li> <li> <p> <code>DELETING</code>: Resolver is deleting this query logging association.</p> </li> <li> <p> <code>FAILED</code>: Resolver either couldn't create or couldn't delete the query logging association.</p> </li> </ul>"""
    error: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_association_error.ResolverQueryLogConfigAssociationError"
    ]
    """<p>If the value of <code>Status</code> is <code>FAILED</code>, the value of <code>Error</code> indicates the cause:</p> <ul> <li> <p> <code>DESTINATION_NOT_FOUND</code>: The specified destination (for example, an Amazon S3 bucket) was deleted.</p> </li> <li> <p> <code>ACCESS_DENIED</code>: Permissions don't allow sending logs to the destination.</p> </li> </ul> <p>If the value of <code>Status</code> is a value other than <code>FAILED</code>, <code>Error</code> is null. </p>"""
    error_message: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_association_error_message.ResolverQueryLogConfigAssociationErrorMessage"
    ]
    """<p>Contains additional information about the error. If the value or <code>Error</code> is null, the value of <code>ErrorMessage</code> also is null.</p>"""
    creation_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the VPC was associated with the query logging configuration, in Unix time format and Coordinated Universal Time (UTC).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverQueryLogConfigAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "resolver_query_log_config_id" in value:
        out["ResolverQueryLogConfigId"] = value["resolver_query_log_config_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "status" in value:
        import aws_sdk_route53resolver.types.resolver_query_log_config_association_status

        out["Status"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_association_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error" in value:
        import aws_sdk_route53resolver.types.resolver_query_log_config_association_error

        out["Error"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_association_error.serialize_aws_json_1_1(
                value["error"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverQueryLogConfigAssociation:
    out: ResolverQueryLogConfigAssociation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ResolverQueryLogConfigId" in data:
        out["resolver_query_log_config_id"] = data["ResolverQueryLogConfigId"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.resolver_query_log_config_association_status

        out["status"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_association_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Error" in data:
        import aws_sdk_route53resolver.types.resolver_query_log_config_association_error

        out["error"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_association_error.deserialize_aws_json_1_1(
                data["Error"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    return out
