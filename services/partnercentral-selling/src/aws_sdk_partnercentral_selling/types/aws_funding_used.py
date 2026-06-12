"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsFundingUsed``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

AwsFundingUsed: TypeAlias = Literal[
    "Yes",
    "No",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Yes",
        "No",
    )
)


def serialize_aws_json_1_0(value: AwsFundingUsed) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsFundingUsed:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AwsFundingUsed value: {data!r}")
    return cast(AwsFundingUsed, data)
