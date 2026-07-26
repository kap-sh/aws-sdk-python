"""Generated from Smithy shape ``com.amazonaws.chime#EventsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.sensitive_string
    import capo_chime.types.string


class EventsConfiguration(TypedDict, closed=True):
    bot_id: NotRequired["capo_chime.types.string.String"]
    """<p>The bot ID.</p>"""
    outbound_events_https_endpoint: NotRequired[
        "capo_chime.types.sensitive_string.SensitiveString"
    ]
    """<p>HTTPS endpoint that allows a bot to receive outgoing events.</p>"""
    lambda_function_arn: NotRequired[
        "capo_chime.types.sensitive_string.SensitiveString"
    ]
    """<p>Lambda function ARN that allows a bot to receive outgoing events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventsConfiguration) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["BotId"] = value["bot_id"]
    if "outbound_events_https_endpoint" in value:
        out["OutboundEventsHTTPSEndpoint"] = value["outbound_events_https_endpoint"]
    if "lambda_function_arn" in value:
        out["LambdaFunctionArn"] = value["lambda_function_arn"]
    return out


def deserialize_json(data: dict) -> EventsConfiguration:
    out: EventsConfiguration = {}  # type: ignore[typeddict-item]
    if "BotId" in data:
        out["bot_id"] = data["BotId"]
    if "OutboundEventsHTTPSEndpoint" in data:
        out["outbound_events_https_endpoint"] = data["OutboundEventsHTTPSEndpoint"]
    if "LambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["LambdaFunctionArn"]
    return out
