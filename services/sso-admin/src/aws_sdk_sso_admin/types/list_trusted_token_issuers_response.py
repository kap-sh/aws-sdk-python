"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListTrustedTokenIssuersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.token
    import aws_sdk_sso_admin.types.trusted_token_issuer_list


class ListTrustedTokenIssuersResponse(TypedDict):
    trusted_token_issuers: NotRequired[
        "aws_sdk_sso_admin.types.trusted_token_issuer_list.TrustedTokenIssuerList"
    ]
    """<p>An array list of the trusted token issuer configurations.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrustedTokenIssuersResponse) -> dict:
    out: dict = {}
    if "trusted_token_issuers" in value:
        import aws_sdk_sso_admin.types.trusted_token_issuer_list

        out["TrustedTokenIssuers"] = (
            aws_sdk_sso_admin.types.trusted_token_issuer_list.serialize_aws_json_1_1(
                value["trusted_token_issuers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrustedTokenIssuersResponse:
    out: ListTrustedTokenIssuersResponse = {}  # type: ignore[typeddict-item]
    if "TrustedTokenIssuers" in data:
        import aws_sdk_sso_admin.types.trusted_token_issuer_list

        out["trusted_token_issuers"] = (
            aws_sdk_sso_admin.types.trusted_token_issuer_list.deserialize_aws_json_1_1(
                data["TrustedTokenIssuers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
