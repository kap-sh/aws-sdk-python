"""Generated from Smithy shape ``com.amazonaws.ssoadmin#SignInOrigin``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

SignInOrigin: TypeAlias = Literal[
    "IDENTITY_CENTER",
    "APPLICATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDENTITY_CENTER",
        "APPLICATION",
    )
)


def serialize_aws_json_1_1(value: SignInOrigin) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SignInOrigin:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SignInOrigin value: {data!r}")
    return cast(SignInOrigin, data)
