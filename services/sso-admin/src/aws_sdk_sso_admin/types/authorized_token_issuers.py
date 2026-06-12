"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthorizedTokenIssuers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.authorized_token_issuer

AuthorizedTokenIssuers: TypeAlias = list[
    "aws_sdk_sso_admin.types.authorized_token_issuer.AuthorizedTokenIssuer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizedTokenIssuers) -> list:
    import aws_sdk_sso_admin.types.authorized_token_issuer

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.authorized_token_issuer.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AuthorizedTokenIssuers:
    import aws_sdk_sso_admin.types.authorized_token_issuer

    out: AuthorizedTokenIssuers = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.authorized_token_issuer.deserialize_aws_json_1_1(
                item
            )
        )
    return out
