"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateResolverQueryLogConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.destination_arn
    import aws_sdk_route53resolver.types.resolver_query_log_config_name
    import aws_sdk_route53resolver.types.tag_list


class CreateResolverQueryLogConfigRequest(TypedDict):
    name: "aws_sdk_route53resolver.types.resolver_query_log_config_name.ResolverQueryLogConfigName"
    """<p>The name that you want to give the query logging configuration.</p>"""
    destination_arn: "aws_sdk_route53resolver.types.destination_arn.DestinationArn"
    """<p>The ARN of the resource that you want Resolver to send query logs. You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream. Examples of valid values include the following:</p> <ul> <li> <p> <b>S3 bucket</b>: </p> <p> <code>arn:aws:s3:::amzn-s3-demo-bucket</code> </p> <p>You can optionally append a file prefix to the end of the ARN.</p> <p> <code>arn:aws:s3:::amzn-s3-demo-bucket/development/</code> </p> </li> <li> <p> <b>CloudWatch Logs log group</b>: </p> <p> <code>arn:aws:logs:us-west-1:123456789012:log-group:/mystack-testgroup-12ABC1AB12A1:*</code> </p> </li> <li> <p> <b>Kinesis Data Firehose delivery stream</b>:</p> <p> <code>arn:aws:kinesis:us-east-2:0123456789:stream/my_stream_name</code> </p> </li> </ul>"""
    creator_request_id: (
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    )
    """<p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>"""
    tags: NotRequired["aws_sdk_route53resolver.types.tag_list.TagList"]
    """<p>A list of the tag keys and values that you want to associate with the query logging configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResolverQueryLogConfigRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["DestinationArn"] = value["destination_arn"]
    out["CreatorRequestId"] = value["creator_request_id"]
    if "tags" in value:
        import aws_sdk_route53resolver.types.tag_list

        out["Tags"] = aws_sdk_route53resolver.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResolverQueryLogConfigRequest:
    out: CreateResolverQueryLogConfigRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateResolverQueryLogConfigRequest.name required")
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    else:
        raise DeserializationError(
            "CreateResolverQueryLogConfigRequest.destination_arn required"
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    else:
        raise DeserializationError(
            "CreateResolverQueryLogConfigRequest.creator_request_id required"
        )
    if "Tags" in data:
        import aws_sdk_route53resolver.types.tag_list

        out["tags"] = aws_sdk_route53resolver.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
