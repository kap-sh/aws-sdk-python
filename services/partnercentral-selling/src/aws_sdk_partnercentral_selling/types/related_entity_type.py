"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#RelatedEntityType``."""

from typing import Literal, TypeAlias, cast

RelatedEntityType: TypeAlias = Literal[
    "Solutions",
    "AwsProducts",
    "AwsMarketplaceOffers",
    "AwsMarketplaceOfferSets",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelatedEntityType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RelatedEntityType:
    return cast(RelatedEntityType, data)
