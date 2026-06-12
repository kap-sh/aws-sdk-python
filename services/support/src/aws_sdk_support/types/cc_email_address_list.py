"""Generated from Smithy shape ``com.amazonaws.support#CcEmailAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.cc_email_address

CcEmailAddressList: TypeAlias = list[
    "aws_sdk_support.types.cc_email_address.CcEmailAddress"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CcEmailAddressList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CcEmailAddressList:
    return list(data)
