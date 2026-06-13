"""Generated from Smithy shape ``com.amazonaws.mailmanager#TlsPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

TlsPolicy: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
    "FIPS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED",
        "OPTIONAL",
        "FIPS",
    )
)


def serialize_aws_json_1_0(value: TlsPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TlsPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TlsPolicy value: {data!r}")
    return cast(TlsPolicy, data)
