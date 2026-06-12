"""Generated from Smithy shape ``com.amazonaws.health#awsAccountIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.account_id

awsAccountIdsList: TypeAlias = list["aws_sdk_health.types.account_id.accountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: awsAccountIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> awsAccountIdsList:
    return list(data)
