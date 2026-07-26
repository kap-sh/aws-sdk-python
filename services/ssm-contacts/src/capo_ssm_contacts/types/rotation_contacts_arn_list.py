"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationContactsArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn

RotationContactsArnList: TypeAlias = list[
    "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationContactsArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RotationContactsArnList:
    return list(data)
