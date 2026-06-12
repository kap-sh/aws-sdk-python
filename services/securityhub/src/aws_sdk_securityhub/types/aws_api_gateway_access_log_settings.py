"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayAccessLogSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsApiGatewayAccessLogSettings(TypedDict):
    format: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A single-line format of the access logs of data, as specified by selected <code>$context</code> variables. The format must include at least <code>$context.requestId</code>.</p>"""
    destination_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the CloudWatch Logs log group that receives the access logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayAccessLogSettings) -> dict:
    out: dict = {}
    if "format" in value:
        out["Format"] = value["format"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    return out


def deserialize_json(data: dict) -> AwsApiGatewayAccessLogSettings:
    out: AwsApiGatewayAccessLogSettings = {}  # type: ignore[typeddict-item]
    if "Format" in data:
        out["format"] = data["Format"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    return out
