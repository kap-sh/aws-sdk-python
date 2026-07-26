"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#SubscribeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_notifications.types.client_request_token
    import capo_codestar_notifications.types.notification_rule_arn
    import capo_codestar_notifications.types.target


class SubscribeRequest(TypedDict, closed=True):
    arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    """<p>The Amazon Resource Name (ARN) of the notification rule for which you want to create the association.</p>"""
    target: "capo_codestar_notifications.types.target.Target"
    client_request_token: NotRequired[
        "capo_codestar_notifications.types.client_request_token.ClientRequestToken"
    ]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribeRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_codestar_notifications.types.target

    out["Target"] = capo_codestar_notifications.types.target.serialize_json(
        value["target"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> SubscribeRequest:
    out: SubscribeRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("SubscribeRequest.arn required")
    if "Target" in data:
        import capo_codestar_notifications.types.target

        out["target"] = capo_codestar_notifications.types.target.deserialize_json(
            data["Target"]
        )
    else:
        raise DeserializationError("SubscribeRequest.target required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
