"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DeleteAppInstanceBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn


class DeleteAppInstanceBotRequest(TypedDict):
    app_instance_bot_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceBot</code> being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppInstanceBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppInstanceBotRequest:
    out: DeleteAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
    return out
