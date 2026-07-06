"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointConnectionLogOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2ClientVpnEndpointConnectionLogOptionsDetails(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether client connection logging is enabled for the Client VPN endpoint. </p>"""
    cloudwatch_log_group: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the Amazon CloudWatch Logs log group to which connection logging data is published. </p>"""
    cloudwatch_log_stream: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the Amazon CloudWatch Logs log stream to which connection logging data is published. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2ClientVpnEndpointConnectionLogOptionsDetails) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "cloudwatch_log_group" in value:
        out["CloudwatchLogGroup"] = value["cloudwatch_log_group"]
    if "cloudwatch_log_stream" in value:
        out["CloudwatchLogStream"] = value["cloudwatch_log_stream"]
    return out


def deserialize_json(data: dict) -> AwsEc2ClientVpnEndpointConnectionLogOptionsDetails:
    out: AwsEc2ClientVpnEndpointConnectionLogOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "CloudwatchLogGroup" in data:
        out["cloudwatch_log_group"] = data["CloudwatchLogGroup"]
    if "CloudwatchLogStream" in data:
        out["cloudwatch_log_stream"] = data["CloudwatchLogStream"]
    return out
