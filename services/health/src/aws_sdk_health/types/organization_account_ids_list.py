"""Generated from Smithy shape ``com.amazonaws.health#OrganizationAccountIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.account_id

OrganizationAccountIdsList: TypeAlias = list[
    "aws_sdk_health.types.account_id.accountId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationAccountIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationAccountIdsList:
    return list(data)
