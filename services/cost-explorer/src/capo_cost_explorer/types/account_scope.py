"""Generated from Smithy shape ``com.amazonaws.costexplorer#AccountScope``."""

from typing import Literal, TypeAlias, cast

AccountScope: TypeAlias = Literal[
    "PAYER",
    "LINKED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountScope:
    return cast(AccountScope, data)
