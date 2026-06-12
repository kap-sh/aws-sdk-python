"""Generated from Smithy shape ``com.amazonaws.ssoadmin#JwtBearerGrant``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.authorized_token_issuers


class JwtBearerGrant(TypedDict):
    authorized_token_issuers: NotRequired[
        "aws_sdk_sso_admin.types.authorized_token_issuers.AuthorizedTokenIssuers"
    ]
    """<p>A list of allowed token issuers trusted by the Identity Center instances for this application.</p> <note> <p> <code>AuthorizedTokenIssuers</code> is required when the grant type is <code>JwtBearerGrant</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JwtBearerGrant) -> dict:
    out: dict = {}
    if "authorized_token_issuers" in value:
        import aws_sdk_sso_admin.types.authorized_token_issuers

        out["AuthorizedTokenIssuers"] = (
            aws_sdk_sso_admin.types.authorized_token_issuers.serialize_aws_json_1_1(
                value["authorized_token_issuers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JwtBearerGrant:
    out: JwtBearerGrant = {}  # type: ignore[typeddict-item]
    if "AuthorizedTokenIssuers" in data:
        import aws_sdk_sso_admin.types.authorized_token_issuers

        out["authorized_token_issuers"] = (
            aws_sdk_sso_admin.types.authorized_token_issuers.deserialize_aws_json_1_1(
                data["AuthorizedTokenIssuers"]
            )
        )
    return out
