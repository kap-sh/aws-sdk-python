"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_product_identifier

AwsProductIdentifiers: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_product_identifier.AwsProductIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AwsProductIdentifiers:
    return list(data)
