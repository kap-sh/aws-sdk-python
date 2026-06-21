"""Generated from Smithy shape ``com.amazonaws.pcs#AccountingMode``."""

from typing import Literal, TypeAlias, cast

AccountingMode: TypeAlias = Literal[
    "STANDARD",
    "NONE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccountingMode:
    return cast(AccountingMode, data)
