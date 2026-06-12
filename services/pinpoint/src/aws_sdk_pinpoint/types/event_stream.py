"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventStream``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class EventStream(TypedDict):
    application_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application to publish event data for.</p>"""
    destination_stream_arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Kinesis data stream or Amazon Kinesis Data Firehose delivery stream to publish event data to.</p> <p>For a Kinesis data stream, the ARN format is: arn:aws:kinesis:<replaceable>region</replaceable>:<replaceable>account-id</replaceable>:stream/<replaceable>stream_name</replaceable> </p> <p>For a Kinesis Data Firehose delivery stream, the ARN format is: arn:aws:firehose:<replaceable>region</replaceable>:<replaceable>account-id</replaceable>:deliverystream/<replaceable>stream_name</replaceable> </p>"""
    external_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>(Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when publishing event data, but we removed this requirement. We don't recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint.</p>"""
    last_modified_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the event stream was last modified.</p>"""
    last_updated_by: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The IAM user who last modified the event stream.</p>"""
    role_arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to publish event data to the stream in your AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventStream) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "destination_stream_arn" in value:
        out["DestinationStreamArn"] = value["destination_stream_arn"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "last_updated_by" in value:
        out["LastUpdatedBy"] = value["last_updated_by"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> EventStream:
    out: EventStream = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "DestinationStreamArn" in data:
        out["destination_stream_arn"] = data["DestinationStreamArn"]
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "LastUpdatedBy" in data:
        out["last_updated_by"] = data["LastUpdatedBy"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
