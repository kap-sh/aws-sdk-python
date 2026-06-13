"""Generated from Smithy shape ``com.amazonaws.qbusiness#IdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

IdentityType: TypeAlias = Literal[
    "AWS_IAM_IDP_SAML",
    "AWS_IAM_IDP_OIDC",
    "AWS_IAM_IDC",
    "AWS_QUICKSIGHT_IDP",
    "ANONYMOUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_IAM_IDP_SAML",
        "AWS_IAM_IDP_OIDC",
        "AWS_IAM_IDC",
        "AWS_QUICKSIGHT_IDP",
        "ANONYMOUS",
    )
)


def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityType value: {data!r}")
    return cast(IdentityType, data)
