"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsMarketplaceOfferSetIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_marketplace_offer_set_identifier

AwsMarketplaceOfferSetIdentifiers: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.aws_marketplace_offer_set_identifier.AwsMarketplaceOfferSetIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsMarketplaceOfferSetIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AwsMarketplaceOfferSetIdentifiers:
    return list(data)
