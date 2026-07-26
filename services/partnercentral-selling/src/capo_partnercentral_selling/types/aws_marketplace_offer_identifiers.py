"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsMarketplaceOfferIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_marketplace_offer_identifier

AwsMarketplaceOfferIdentifiers: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_marketplace_offer_identifier.AwsMarketplaceOfferIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsMarketplaceOfferIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AwsMarketplaceOfferIdentifiers:
    return list(data)
