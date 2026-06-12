"""Generated from Smithy shape ``com.amazonaws.route53resolver#OutpostResolver``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.arn
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.instance_count
    import aws_sdk_route53resolver.types.outpost_arn
    import aws_sdk_route53resolver.types.outpost_instance_type
    import aws_sdk_route53resolver.types.outpost_resolver_name
    import aws_sdk_route53resolver.types.outpost_resolver_status
    import aws_sdk_route53resolver.types.outpost_resolver_status_message
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.rfc3339_time_string


class OutpostResolver(TypedDict):
    arn: NotRequired["aws_sdk_route53resolver.types.arn.Arn"]
    """<p>The ARN (Amazon Resource Name) for the Resolver on an Outpost.</p>"""
    creation_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the Outpost Resolver was created, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    modification_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the Outpost Resolver was modified, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string that identifies the request that created the Resolver endpoint. The <code>CreatorRequestId</code> allows failed requests to be retried without the risk of running the operation twice.</p>"""
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the Resolver on Outpost.</p>"""
    instance_count: NotRequired[
        "aws_sdk_route53resolver.types.instance_count.InstanceCount"
    ]
    """<p>Amazon EC2 instance count for the Resolver on the Outpost.</p>"""
    preferred_instance_type: NotRequired[
        "aws_sdk_route53resolver.types.outpost_instance_type.OutpostInstanceType"
    ]
    """<p> The Amazon EC2 instance type. </p>"""
    name: NotRequired[
        "aws_sdk_route53resolver.types.outpost_resolver_name.OutpostResolverName"
    ]
    """<p>Name of the Resolver.</p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.outpost_resolver_status.OutpostResolverStatus"
    ]
    """<p>Status of the Resolver.</p>"""
    status_message: NotRequired[
        "aws_sdk_route53resolver.types.outpost_resolver_status_message.OutpostResolverStatusMessage"
    ]
    """<p>A detailed description of the Resolver.</p>"""
    outpost_arn: NotRequired["aws_sdk_route53resolver.types.outpost_arn.OutpostArn"]
    """<p>The ARN (Amazon Resource Name) for the Outpost.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutpostResolver) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "preferred_instance_type" in value:
        out["PreferredInstanceType"] = value["preferred_instance_type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_route53resolver.types.outpost_resolver_status

        out["Status"] = (
            aws_sdk_route53resolver.types.outpost_resolver_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutpostResolver:
    out: OutpostResolver = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "ModificationTime" in data:
        out["modification_time"] = data["ModificationTime"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "PreferredInstanceType" in data:
        out["preferred_instance_type"] = data["PreferredInstanceType"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.outpost_resolver_status

        out["status"] = (
            aws_sdk_route53resolver.types.outpost_resolver_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    return out
