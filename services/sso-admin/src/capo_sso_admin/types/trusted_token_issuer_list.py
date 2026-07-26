"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TrustedTokenIssuerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.trusted_token_issuer_metadata

TrustedTokenIssuerList: TypeAlias = list[
    "capo_sso_admin.types.trusted_token_issuer_metadata.TrustedTokenIssuerMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedTokenIssuerList) -> list:
    import capo_sso_admin.types.trusted_token_issuer_metadata

    out: list = []
    for item in value:
        out.append(
            capo_sso_admin.types.trusted_token_issuer_metadata.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrustedTokenIssuerList:
    import capo_sso_admin.types.trusted_token_issuer_metadata

    out: TrustedTokenIssuerList = []
    for item in data:
        out.append(
            capo_sso_admin.types.trusted_token_issuer_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
