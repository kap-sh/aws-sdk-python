"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Intent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

Intent: TypeAlias = Literal[
    "NEW",
    "AMEND",
    "REPLACE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "AMEND",
        "REPLACE",
    )
)


def serialize_aws_json_1_0(value: Intent) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Intent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Intent value: {data!r}")
    return cast(Intent, data)
