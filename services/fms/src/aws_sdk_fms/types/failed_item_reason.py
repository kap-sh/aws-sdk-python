"""Generated from Smithy shape ``com.amazonaws.fms#FailedItemReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

FailedItemReason: TypeAlias = Literal[
    "NOT_VALID_ARN",
    "NOT_VALID_PARTITION",
    "NOT_VALID_REGION",
    "NOT_VALID_SERVICE",
    "NOT_VALID_RESOURCE_TYPE",
    "NOT_VALID_ACCOUNT_ID",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_VALID_ARN",
        "NOT_VALID_PARTITION",
        "NOT_VALID_REGION",
        "NOT_VALID_SERVICE",
        "NOT_VALID_RESOURCE_TYPE",
        "NOT_VALID_ACCOUNT_ID",
    )
)


def serialize_aws_json_1_1(value: FailedItemReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailedItemReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailedItemReason value: {data!r}")
    return cast(FailedItemReason, data)
