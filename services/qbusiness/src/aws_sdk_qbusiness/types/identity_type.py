"""Generated from Smithy shape ``com.amazonaws.qbusiness#IdentityType``."""

from typing import Literal, TypeAlias, cast

IdentityType: TypeAlias = Literal[
    "AWS_IAM_IDP_SAML",
    "AWS_IAM_IDP_OIDC",
    "AWS_IAM_IDC",
    "AWS_QUICKSIGHT_IDP",
    "ANONYMOUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    return cast(IdentityType, data)
