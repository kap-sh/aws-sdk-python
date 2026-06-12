"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#WhatsAppOutboundConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn


class WhatsAppOutboundConfig(TypedDict):
    connect_source_phone_number_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"
    wisdom_template_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppOutboundConfig) -> dict:
    out: dict = {}
    out["connectSourcePhoneNumberArn"] = value["connect_source_phone_number_arn"]
    out["wisdomTemplateArn"] = value["wisdom_template_arn"]
    return out


def deserialize_json(data: dict) -> WhatsAppOutboundConfig:
    out: WhatsAppOutboundConfig = {}  # type: ignore[typeddict-item]
    if "connectSourcePhoneNumberArn" in data:
        out["connect_source_phone_number_arn"] = data["connectSourcePhoneNumberArn"]
    else:
        raise DeserializationError(
            "WhatsAppOutboundConfig.connect_source_phone_number_arn required"
        )
    if "wisdomTemplateArn" in data:
        out["wisdom_template_arn"] = data["wisdomTemplateArn"]
    else:
        raise DeserializationError(
            "WhatsAppOutboundConfig.wisdom_template_arn required"
        )
    return out
