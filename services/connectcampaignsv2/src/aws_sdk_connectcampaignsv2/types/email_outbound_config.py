"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#EmailOutboundConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn
    import aws_sdk_connectcampaignsv2.types.email_address
    import aws_sdk_connectcampaignsv2.types.email_display_name


class EmailOutboundConfig(TypedDict):
    connect_source_email_address: (
        "aws_sdk_connectcampaignsv2.types.email_address.EmailAddress"
    )
    source_email_address_display_name: NotRequired[
        "aws_sdk_connectcampaignsv2.types.email_display_name.EmailDisplayName"
    ]
    wisdom_template_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: EmailOutboundConfig) -> dict:
    out: dict = {}
    out["connectSourceEmailAddress"] = value["connect_source_email_address"]
    if "source_email_address_display_name" in value:
        out["sourceEmailAddressDisplayName"] = value[
            "source_email_address_display_name"
        ]
    out["wisdomTemplateArn"] = value["wisdom_template_arn"]
    return out


def deserialize_json(data: dict) -> EmailOutboundConfig:
    out: EmailOutboundConfig = {}  # type: ignore[typeddict-item]
    if "connectSourceEmailAddress" in data:
        out["connect_source_email_address"] = data["connectSourceEmailAddress"]
    else:
        raise DeserializationError(
            "EmailOutboundConfig.connect_source_email_address required"
        )
    if "sourceEmailAddressDisplayName" in data:
        out["source_email_address_display_name"] = data["sourceEmailAddressDisplayName"]
    if "wisdomTemplateArn" in data:
        out["wisdom_template_arn"] = data["wisdomTemplateArn"]
    else:
        raise DeserializationError("EmailOutboundConfig.wisdom_template_arn required")
    return out
