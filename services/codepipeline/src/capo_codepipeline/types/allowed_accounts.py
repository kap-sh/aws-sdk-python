"""Generated from Smithy shape ``com.amazonaws.codepipeline#AllowedAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.allowed_account

AllowedAccounts: TypeAlias = list[
    "capo_codepipeline.types.allowed_account.AllowedAccount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedAccounts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AllowedAccounts:
    return list(data)
