"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyChannelSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class JourneyChannelSettings(TypedDict, closed=True):
    connect_campaign_arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Amazon Resource Name (ARN) of the Connect Campaign.</p>"""
    connect_campaign_execution_role_arn: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>IAM role ARN to be assumed when invoking Connect campaign execution APIs for dialing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyChannelSettings) -> dict:
    out: dict = {}
    if "connect_campaign_arn" in value:
        out["ConnectCampaignArn"] = value["connect_campaign_arn"]
    if "connect_campaign_execution_role_arn" in value:
        out["ConnectCampaignExecutionRoleArn"] = value[
            "connect_campaign_execution_role_arn"
        ]
    return out


def deserialize_json(data: dict) -> JourneyChannelSettings:
    out: JourneyChannelSettings = {}  # type: ignore[typeddict-item]
    if "ConnectCampaignArn" in data:
        out["connect_campaign_arn"] = data["ConnectCampaignArn"]
    if "ConnectCampaignExecutionRoleArn" in data:
        out["connect_campaign_execution_role_arn"] = data[
            "ConnectCampaignExecutionRoleArn"
        ]
    return out
