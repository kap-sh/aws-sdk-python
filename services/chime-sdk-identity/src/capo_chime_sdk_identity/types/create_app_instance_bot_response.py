"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn


class CreateAppInstanceBotResponse(TypedDict, closed=True):
    app_instance_bot_arn: NotRequired[
        "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppinstanceBot</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceBotResponse) -> dict:
    out: dict = {}
    if "app_instance_bot_arn" in value:
        out["AppInstanceBotArn"] = value["app_instance_bot_arn"]
    return out


def deserialize_json(data: dict) -> CreateAppInstanceBotResponse:
    out: CreateAppInstanceBotResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceBotArn" in data:
        out["app_instance_bot_arn"] = data["AppInstanceBotArn"]
    return out
