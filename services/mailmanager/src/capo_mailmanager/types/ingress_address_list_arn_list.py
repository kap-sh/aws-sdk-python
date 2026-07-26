"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressAddressListArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.address_list_arn

IngressAddressListArnList: TypeAlias = list[
    "capo_mailmanager.types.address_list_arn.AddressListArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressAddressListArnList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> IngressAddressListArnList:
    return list(data)
