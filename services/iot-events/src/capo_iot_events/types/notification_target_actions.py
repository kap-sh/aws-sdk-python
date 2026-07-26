"""Generated from Smithy shape ``com.amazonaws.iotevents#NotificationTargetActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.lambda_action


class NotificationTargetActions(TypedDict, closed=True):
    lambda_action: NotRequired["capo_iot_events.types.lambda_action.LambdaAction"]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationTargetActions) -> dict:
    out: dict = {}
    if "lambda_action" in value:
        import capo_iot_events.types.lambda_action

        out["lambdaAction"] = capo_iot_events.types.lambda_action.serialize_json(
            value["lambda_action"]
        )
    return out


def deserialize_json(data: dict) -> NotificationTargetActions:
    out: NotificationTargetActions = {}  # type: ignore[typeddict-item]
    if "lambdaAction" in data:
        import capo_iot_events.types.lambda_action

        out["lambda_action"] = capo_iot_events.types.lambda_action.deserialize_json(
            data["lambdaAction"]
        )
    return out
