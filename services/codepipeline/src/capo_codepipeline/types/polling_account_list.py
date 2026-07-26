"""Generated from Smithy shape ``com.amazonaws.codepipeline#PollingAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.account_id

PollingAccountList: TypeAlias = list["capo_codepipeline.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollingAccountList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PollingAccountList:
    return list(data)
