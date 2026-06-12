"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

ConnectionType: TypeAlias = Literal[
    "OPPORTUNITY_COLLABORATION",
    "SUBSIDIARY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPPORTUNITY_COLLABORATION",
        "SUBSIDIARY",
    )
)


def serialize_aws_json_1_0(value: ConnectionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionType value: {data!r}")
    return cast(ConnectionType, data)
