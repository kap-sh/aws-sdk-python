"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

AccessType: TypeAlias = Literal[
    "ALLOW_ALL",
    "DENY_ALL",
    "ALLOW_BY_DEFAULT_DENY_SOME",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW_ALL",
        "DENY_ALL",
        "ALLOW_BY_DEFAULT_DENY_SOME",
    )
)


def serialize_aws_json_1_0(value: AccessType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessType value: {data!r}")
    return cast(AccessType, data)
