"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#RelatedEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

RelatedEntityType: TypeAlias = Literal[
    "Solutions",
    "AwsProducts",
    "AwsMarketplaceOffers",
    "AwsMarketplaceOfferSets",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Solutions",
        "AwsProducts",
        "AwsMarketplaceOffers",
        "AwsMarketplaceOfferSets",
    )
)


def serialize_aws_json_1_0(value: RelatedEntityType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RelatedEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelatedEntityType value: {data!r}")
    return cast(RelatedEntityType, data)
