"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SmsOutboundConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn


class SmsOutboundConfig(TypedDict, closed=True):
    connect_source_phone_number_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"
    wisdom_template_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: SmsOutboundConfig) -> dict:
    out: dict = {}
    out["connectSourcePhoneNumberArn"] = value["connect_source_phone_number_arn"]
    out["wisdomTemplateArn"] = value["wisdom_template_arn"]
    return out


def deserialize_json(data: dict) -> SmsOutboundConfig:
    out: SmsOutboundConfig = {}  # type: ignore[typeddict-item]
    if "connectSourcePhoneNumberArn" in data:
        out["connect_source_phone_number_arn"] = data["connectSourcePhoneNumberArn"]
    else:
        raise DeserializationError(
            "SmsOutboundConfig.connect_source_phone_number_arn required"
        )
    if "wisdomTemplateArn" in data:
        out["wisdom_template_arn"] = data["wisdomTemplateArn"]
    else:
        raise DeserializationError("SmsOutboundConfig.wisdom_template_arn required")
    return out
