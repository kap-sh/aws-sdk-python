"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleAddressListArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address_list_arn

RuleAddressListArnList: TypeAlias = list[
    "aws_sdk_mailmanager.types.address_list_arn.AddressListArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleAddressListArnList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RuleAddressListArnList:
    return list(data)
