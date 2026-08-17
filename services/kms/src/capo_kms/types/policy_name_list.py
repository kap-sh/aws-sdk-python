"""Generated from Smithy shape ``com.amazonaws.kms#PolicyNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.policy_name_type

PolicyNameList: TypeAlias = list["capo_kms.types.policy_name_type.PolicyNameType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PolicyNameList:
    return [item for item in data if item is not None]
