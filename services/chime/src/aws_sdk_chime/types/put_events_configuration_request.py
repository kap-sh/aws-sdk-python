"""Generated from Smithy shape ``com.amazonaws.chime#PutEventsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.sensitive_string


class PutEventsConfigurationRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The bot ID.</p>"""
    outbound_events_https_endpoint: NotRequired[
        "aws_sdk_chime.types.sensitive_string.SensitiveString"
    ]
    """<p>HTTPS endpoint that allows the bot to receive outgoing events.</p>"""
    lambda_function_arn: NotRequired[
        "aws_sdk_chime.types.sensitive_string.SensitiveString"
    ]
    """<p>Lambda function ARN that allows the bot to receive outgoing events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEventsConfigurationRequest) -> dict:
    out: dict = {}
    if "outbound_events_https_endpoint" in value:
        out["OutboundEventsHTTPSEndpoint"] = value["outbound_events_https_endpoint"]
    if "lambda_function_arn" in value:
        out["LambdaFunctionArn"] = value["lambda_function_arn"]
    return out


def deserialize_json(data: dict) -> PutEventsConfigurationRequest:
    out: PutEventsConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "OutboundEventsHTTPSEndpoint" in data:
        out["outbound_events_https_endpoint"] = data["OutboundEventsHTTPSEndpoint"]
    if "LambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["LambdaFunctionArn"]
    return out
