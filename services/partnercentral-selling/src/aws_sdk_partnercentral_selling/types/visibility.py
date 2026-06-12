"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Visibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

Visibility: TypeAlias = Literal[
    "Full",
    "Limited",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Full",
        "Limited",
    )
)


def serialize_aws_json_1_0(value: Visibility) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Visibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Visibility value: {data!r}")
    return cast(Visibility, data)
