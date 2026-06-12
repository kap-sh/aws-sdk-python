"""Generated from Smithy shape ``com.amazonaws.iotevents#NotificationTargetActions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.lambda_action


class NotificationTargetActions(TypedDict):
    lambda_action: NotRequired["aws_sdk_iot_events.types.lambda_action.LambdaAction"]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationTargetActions) -> dict:
    out: dict = {}
    if "lambda_action" in value:
        import aws_sdk_iot_events.types.lambda_action

        out["lambdaAction"] = aws_sdk_iot_events.types.lambda_action.serialize_json(
            value["lambda_action"]
        )
    return out


def deserialize_json(data: dict) -> NotificationTargetActions:
    out: NotificationTargetActions = {}  # type: ignore[typeddict-item]
    if "lambdaAction" in data:
        import aws_sdk_iot_events.types.lambda_action

        out["lambda_action"] = aws_sdk_iot_events.types.lambda_action.deserialize_json(
            data["lambdaAction"]
        )
    return out
