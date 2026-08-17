"""Generated from Smithy shape ``com.amazonaws.kms#GrantTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.grant_token_type

GrantTokenList: TypeAlias = list["capo_kms.types.grant_token_type.GrantTokenType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantTokenList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GrantTokenList:
    return [item for item in data if item is not None]
