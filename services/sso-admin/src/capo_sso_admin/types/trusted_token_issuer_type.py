"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TrustedTokenIssuerType``."""

from typing import Literal, TypeAlias, cast

TrustedTokenIssuerType: TypeAlias = Literal["OIDC_JWT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedTokenIssuerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustedTokenIssuerType:
    return cast(TrustedTokenIssuerType, data)
