"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelBanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class CreateChannelBanRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the ban request.</p>"""
    member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the member being banned.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelBanRequest) -> dict:
    out: dict = {}
    out["MemberArn"] = value["member_arn"]
    return out


def deserialize_json(data: dict) -> CreateChannelBanRequest:
    out: CreateChannelBanRequest = {}  # type: ignore[typeddict-item]
    if "MemberArn" in data:
        out["member_arn"] = data["MemberArn"]
    else:
        raise DeserializationError("CreateChannelBanRequest.member_arn required")
    return out
