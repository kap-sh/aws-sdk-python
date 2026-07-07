"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#EmailChannelSubtypeParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn
    import aws_sdk_connectcampaignsv2.types.attributes
    import aws_sdk_connectcampaignsv2.types.email_address


class EmailChannelSubtypeParameters(TypedDict, closed=True):
    destination_email_address: (
        "aws_sdk_connectcampaignsv2.types.email_address.EmailAddress"
    )
    connect_source_email_address: NotRequired[
        "aws_sdk_connectcampaignsv2.types.email_address.EmailAddress"
    ]
    template_arn: NotRequired["aws_sdk_connectcampaignsv2.types.arn.Arn"]
    template_parameters: "aws_sdk_connectcampaignsv2.types.attributes.Attributes"


# --- restJson1 ser/de ---
def serialize_json(value: EmailChannelSubtypeParameters) -> dict:
    out: dict = {}
    out["destinationEmailAddress"] = value["destination_email_address"]
    if "connect_source_email_address" in value:
        out["connectSourceEmailAddress"] = value["connect_source_email_address"]
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    import aws_sdk_connectcampaignsv2.types.attributes

    out["templateParameters"] = (
        aws_sdk_connectcampaignsv2.types.attributes.serialize_json(
            value["template_parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> EmailChannelSubtypeParameters:
    out: EmailChannelSubtypeParameters = {}  # type: ignore[typeddict-item]
    if "destinationEmailAddress" in data:
        out["destination_email_address"] = data["destinationEmailAddress"]
    else:
        raise DeserializationError(
            "EmailChannelSubtypeParameters.destination_email_address required"
        )
    if "connectSourceEmailAddress" in data:
        out["connect_source_email_address"] = data["connectSourceEmailAddress"]
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    if "templateParameters" in data:
        import aws_sdk_connectcampaignsv2.types.attributes

        out["template_parameters"] = (
            aws_sdk_connectcampaignsv2.types.attributes.deserialize_json(
                data["templateParameters"]
            )
        )
    else:
        raise DeserializationError(
            "EmailChannelSubtypeParameters.template_parameters required"
        )
    return out
