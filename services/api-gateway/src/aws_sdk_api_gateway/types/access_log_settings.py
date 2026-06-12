"""Generated from Smithy shape ``com.amazonaws.apigateway#AccessLogSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class AccessLogSettings(TypedDict):
    format: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>A single line format of the access logs of data, as specified by selected $context variables. The format must include at least <code>$context.requestId</code>.</p>"""
    destination_arn: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch Logs log group or Kinesis Data Firehose delivery stream to receive access logs. If you specify a Kinesis Data Firehose delivery stream, the stream name must begin with <code>amazon-apigateway-</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessLogSettings) -> dict:
    out: dict = {}
    if "format" in value:
        out["format"] = value["format"]
    if "destination_arn" in value:
        out["destinationArn"] = value["destination_arn"]
    return out


def deserialize_json(data: dict) -> AccessLogSettings:
    out: AccessLogSettings = {}  # type: ignore[typeddict-item]
    if "format" in data:
        out["format"] = data["format"]
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    return out
