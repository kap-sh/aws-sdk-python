"""Generated from Smithy shape ``com.amazonaws.sagemaker#VpcOnlyTrustedAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.account_id

VpcOnlyTrustedAccounts: TypeAlias = list["capo_sagemaker.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcOnlyTrustedAccounts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VpcOnlyTrustedAccounts:
    return list(data)
