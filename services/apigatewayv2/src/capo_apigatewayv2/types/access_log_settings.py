"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#AccessLogSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.arn
    import capo_apigatewayv2.types.string_with_length_between1_and1024


class AccessLogSettings(TypedDict, closed=True):
    destination_arn: NotRequired["capo_apigatewayv2.types.arn.Arn"]
    """<p>The ARN of the CloudWatch Logs log group to receive access logs.</p>"""
    format: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and1024.StringWithLengthBetween1And1024"
    ]
    """<p>A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessLogSettings) -> dict:
    out: dict = {}
    if "destination_arn" in value:
        out["destinationArn"] = value["destination_arn"]
    if "format" in value:
        out["format"] = value["format"]
    return out


def deserialize_json(data: dict) -> AccessLogSettings:
    out: AccessLogSettings = {}  # type: ignore[typeddict-item]
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    if "format" in data:
        out["format"] = data["format"]
    return out
