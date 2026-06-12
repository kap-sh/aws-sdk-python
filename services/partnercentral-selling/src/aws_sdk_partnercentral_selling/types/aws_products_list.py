"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_product_details

AwsProductsList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.aws_product_details.AwsProductDetails"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductsList) -> list:
    import aws_sdk_partnercentral_selling.types.aws_product_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.aws_product_details.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AwsProductsList:
    import aws_sdk_partnercentral_selling.types.aws_product_details

    out: AwsProductsList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.aws_product_details.deserialize_aws_json_1_0(
                item
            )
        )
    return out
