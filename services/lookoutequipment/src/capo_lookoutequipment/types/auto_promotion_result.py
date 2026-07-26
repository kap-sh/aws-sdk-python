"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#AutoPromotionResult``."""

from typing import Literal, TypeAlias, cast

AutoPromotionResult: TypeAlias = Literal[
    "MODEL_PROMOTED",
    "MODEL_NOT_PROMOTED",
    "RETRAINING_INTERNAL_ERROR",
    "RETRAINING_CUSTOMER_ERROR",
    "RETRAINING_CANCELLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoPromotionResult) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoPromotionResult:
    return cast(AutoPromotionResult, data)
