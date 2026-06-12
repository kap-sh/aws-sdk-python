"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Stage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

Stage: TypeAlias = Literal[
    "Prospect",
    "Qualified",
    "Technical Validation",
    "Business Validation",
    "Committed",
    "Launched",
    "Closed Lost",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Prospect",
        "Qualified",
        "Technical Validation",
        "Business Validation",
        "Committed",
        "Launched",
        "Closed Lost",
    )
)


def serialize_aws_json_1_0(value: Stage) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Stage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Stage value: {data!r}")
    return cast(Stage, data)
