"""Generated from Smithy shape ``com.amazonaws.glue#S3Target``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_name
    import aws_sdk_glue.types.event_queue_arn
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.path
    import aws_sdk_glue.types.path_list


class S3Target(TypedDict):
    path: NotRequired["aws_sdk_glue.types.path.Path"]
    """<p>The path to the Amazon S3 target.</p>"""
    exclusions: NotRequired["aws_sdk_glue.types.path_list.PathList"]
    r"""<p>A list of glob patterns used to exclude from the crawl. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html\">Catalog Tables with a Crawler</a>.</p>"""
    connection_name: NotRequired["aws_sdk_glue.types.connection_name.ConnectionName"]
    """<p>The name of a connection which allows a job or crawler to access data in Amazon S3 within an Amazon Virtual Private Cloud environment (Amazon VPC).</p>"""
    sample_size: NotRequired["aws_sdk_glue.types.nullable_integer.NullableInteger"]
    """<p>Sets the number of files in each leaf folder to be crawled when crawling sample files in a dataset. If not set, all the files are crawled. A valid value is an integer between 1 and 249.</p>"""
    event_queue_arn: NotRequired["aws_sdk_glue.types.event_queue_arn.EventQueueArn"]
    """<p>A valid Amazon SQS ARN. For example, <code>arn:aws:sqs:region:account:sqs</code>.</p>"""
    dlq_event_queue_arn: NotRequired["aws_sdk_glue.types.event_queue_arn.EventQueueArn"]
    """<p>A valid Amazon dead-letter SQS ARN. For example, <code>arn:aws:sqs:region:account:deadLetterQueue</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Target) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "exclusions" in value:
        import aws_sdk_glue.types.path_list

        out["Exclusions"] = aws_sdk_glue.types.path_list.serialize_aws_json_1_1(
            value["exclusions"]
        )
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "sample_size" in value:
        out["SampleSize"] = value["sample_size"]
    if "event_queue_arn" in value:
        out["EventQueueArn"] = value["event_queue_arn"]
    if "dlq_event_queue_arn" in value:
        out["DlqEventQueueArn"] = value["dlq_event_queue_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Target:
    out: S3Target = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    if "Exclusions" in data:
        import aws_sdk_glue.types.path_list

        out["exclusions"] = aws_sdk_glue.types.path_list.deserialize_aws_json_1_1(
            data["Exclusions"]
        )
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "SampleSize" in data:
        out["sample_size"] = data["SampleSize"]
    if "EventQueueArn" in data:
        out["event_queue_arn"] = data["EventQueueArn"]
    if "DlqEventQueueArn" in data:
        out["dlq_event_queue_arn"] = data["DlqEventQueueArn"]
    return out
