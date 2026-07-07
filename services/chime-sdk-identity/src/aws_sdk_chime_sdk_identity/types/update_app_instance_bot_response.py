"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#UpdateAppInstanceBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn


class UpdateAppInstanceBotResponse(TypedDict, closed=True):
    app_instance_bot_arn: NotRequired[
        "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceBot</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppInstanceBotResponse) -> dict:
    out: dict = {}
    if "app_instance_bot_arn" in value:
        out["AppInstanceBotArn"] = value["app_instance_bot_arn"]
    return out


def deserialize_json(data: dict) -> UpdateAppInstanceBotResponse:
    out: UpdateAppInstanceBotResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceBotArn" in data:
        out["app_instance_bot_arn"] = data["AppInstanceBotArn"]
    return out
