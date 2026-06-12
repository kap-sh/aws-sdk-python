"""Generated from Smithy shape ``com.amazonaws.ssoadmin#FederationProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

FederationProtocol: TypeAlias = Literal[
    "SAML",
    "OAUTH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAML",
        "OAUTH",
    )
)


def serialize_aws_json_1_1(value: FederationProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FederationProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FederationProtocol value: {data!r}")
    return cast(FederationProtocol, data)
