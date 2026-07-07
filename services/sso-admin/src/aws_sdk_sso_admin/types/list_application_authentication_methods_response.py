"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationAuthenticationMethodsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.authentication_methods
    import aws_sdk_sso_admin.types.token


class ListApplicationAuthenticationMethodsResponse(TypedDict, closed=True):
    authentication_methods: NotRequired[
        "aws_sdk_sso_admin.types.authentication_methods.AuthenticationMethods"
    ]
    """<p>An array list of authentication methods for the specified application.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationAuthenticationMethodsResponse) -> dict:
    out: dict = {}
    if "authentication_methods" in value:
        import aws_sdk_sso_admin.types.authentication_methods

        out["AuthenticationMethods"] = (
            aws_sdk_sso_admin.types.authentication_methods.serialize_aws_json_1_1(
                value["authentication_methods"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListApplicationAuthenticationMethodsResponse:
    out: ListApplicationAuthenticationMethodsResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationMethods" in data:
        import aws_sdk_sso_admin.types.authentication_methods

        out["authentication_methods"] = (
            aws_sdk_sso_admin.types.authentication_methods.deserialize_aws_json_1_1(
                data["AuthenticationMethods"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
