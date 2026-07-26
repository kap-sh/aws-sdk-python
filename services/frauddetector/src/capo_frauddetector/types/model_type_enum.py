"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelTypeEnum``."""

from typing import Literal, TypeAlias, cast

ModelTypeEnum: TypeAlias = Literal[
    "ONLINE_FRAUD_INSIGHTS",
    "TRANSACTION_FRAUD_INSIGHTS",
    "ACCOUNT_TAKEOVER_INSIGHTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelTypeEnum:
    return cast(ModelTypeEnum, data)
