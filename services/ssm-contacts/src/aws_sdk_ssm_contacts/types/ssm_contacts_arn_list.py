"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#SsmContactsArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn

SsmContactsArnList: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SsmContactsArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SsmContactsArnList:
    return list(data)
