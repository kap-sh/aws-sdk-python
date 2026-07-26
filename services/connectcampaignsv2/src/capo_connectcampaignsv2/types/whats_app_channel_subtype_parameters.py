"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#WhatsAppChannelSubtypeParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.attributes
    import capo_connectcampaignsv2.types.destination_phone_number


class WhatsAppChannelSubtypeParameters(TypedDict, closed=True):
    destination_phone_number: (
        "capo_connectcampaignsv2.types.destination_phone_number.DestinationPhoneNumber"
    )
    connect_source_phone_number_arn: NotRequired[
        "capo_connectcampaignsv2.types.arn.Arn"
    ]
    template_arn: NotRequired["capo_connectcampaignsv2.types.arn.Arn"]
    template_parameters: "capo_connectcampaignsv2.types.attributes.Attributes"


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppChannelSubtypeParameters) -> dict:
    out: dict = {}
    out["destinationPhoneNumber"] = value["destination_phone_number"]
    if "connect_source_phone_number_arn" in value:
        out["connectSourcePhoneNumberArn"] = value["connect_source_phone_number_arn"]
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    import capo_connectcampaignsv2.types.attributes

    out["templateParameters"] = capo_connectcampaignsv2.types.attributes.serialize_json(
        value["template_parameters"]
    )
    return out


def deserialize_json(data: dict) -> WhatsAppChannelSubtypeParameters:
    out: WhatsAppChannelSubtypeParameters = {}  # type: ignore[typeddict-item]
    if "destinationPhoneNumber" in data:
        out["destination_phone_number"] = data["destinationPhoneNumber"]
    else:
        raise DeserializationError(
            "WhatsAppChannelSubtypeParameters.destination_phone_number required"
        )
    if "connectSourcePhoneNumberArn" in data:
        out["connect_source_phone_number_arn"] = data["connectSourcePhoneNumberArn"]
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    if "templateParameters" in data:
        import capo_connectcampaignsv2.types.attributes

        out["template_parameters"] = (
            capo_connectcampaignsv2.types.attributes.deserialize_json(
                data["templateParameters"]
            )
        )
    else:
        raise DeserializationError(
            "WhatsAppChannelSubtypeParameters.template_parameters required"
        )
    return out
