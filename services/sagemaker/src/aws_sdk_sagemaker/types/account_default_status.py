"""Generated from Smithy shape ``com.amazonaws.sagemaker#AccountDefaultStatus``."""

from typing import Literal, TypeAlias, cast

AccountDefaultStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountDefaultStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountDefaultStatus:
    return cast(AccountDefaultStatus, data)
