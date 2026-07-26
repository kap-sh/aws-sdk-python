"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn


class DescribeAppInstanceBotRequest(TypedDict, closed=True):
    app_instance_bot_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceBot</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceBotRequest:
    out: DescribeAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
    return out
