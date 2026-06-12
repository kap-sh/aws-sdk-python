"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#AssociationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

AssociationType: TypeAlias = Literal[
    "DOWNSTREAM_SELLER",
    "END_CUSTOMER",
    "INTERNAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOWNSTREAM_SELLER",
        "END_CUSTOMER",
        "INTERNAL",
    )
)


def serialize_aws_json_1_0(value: AssociationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AssociationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationType value: {data!r}")
    return cast(AssociationType, data)
