"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#CreditCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.credit_code

CreditCodes: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.credit_code.CreditCode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditCodes) -> list:
    import aws_sdk_partnercentral_benefits.types.credit_code

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.credit_code.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CreditCodes:
    import aws_sdk_partnercentral_benefits.types.credit_code

    out: CreditCodes = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.credit_code.deserialize_aws_json_1_0(
                item
            )
        )
    return out
