"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ProvisionTargetType``."""

from typing import Literal, TypeAlias, cast

ProvisionTargetType: TypeAlias = Literal[
    "AWS_ACCOUNT",
    "ALL_PROVISIONED_ACCOUNTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionTargetType:
    return cast(ProvisionTargetType, data)
