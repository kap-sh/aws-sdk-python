"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ExpectedCustomerSpendList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.expected_customer_spend

ExpectedCustomerSpendList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.expected_customer_spend.ExpectedCustomerSpend"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpectedCustomerSpendList) -> list:
    import aws_sdk_partnercentral_selling.types.expected_customer_spend

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.expected_customer_spend.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExpectedCustomerSpendList:
    import aws_sdk_partnercentral_selling.types.expected_customer_spend

    out: ExpectedCustomerSpendList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.expected_customer_spend.deserialize_aws_json_1_0(
                item
            )
        )
    return out
