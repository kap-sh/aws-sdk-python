"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#AutoPromotionResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

AutoPromotionResult: TypeAlias = Literal[
    "MODEL_PROMOTED",
    "MODEL_NOT_PROMOTED",
    "RETRAINING_INTERNAL_ERROR",
    "RETRAINING_CUSTOMER_ERROR",
    "RETRAINING_CANCELLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MODEL_PROMOTED",
        "MODEL_NOT_PROMOTED",
        "RETRAINING_INTERNAL_ERROR",
        "RETRAINING_CUSTOMER_ERROR",
        "RETRAINING_CANCELLED",
    )
)


def serialize_aws_json_1_0(value: AutoPromotionResult) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoPromotionResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoPromotionResult value: {data!r}")
    return cast(AutoPromotionResult, data)
