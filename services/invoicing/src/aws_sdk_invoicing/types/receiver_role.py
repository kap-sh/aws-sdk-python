"""Generated from Smithy shape ``com.amazonaws.invoicing#ReceiverRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

ReceiverRole: TypeAlias = Literal[
    "SELLER",
    "RESELLER",
    "BUYER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELLER",
        "RESELLER",
        "BUYER",
    )
)


def serialize_aws_json_1_0(value: ReceiverRole) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReceiverRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReceiverRole value: {data!r}")
    return cast(ReceiverRole, data)
