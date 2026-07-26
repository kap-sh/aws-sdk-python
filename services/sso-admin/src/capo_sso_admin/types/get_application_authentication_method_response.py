"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationAuthenticationMethodResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.authentication_method


class GetApplicationAuthenticationMethodResponse(TypedDict, closed=True):
    authentication_method: NotRequired[
        "capo_sso_admin.types.authentication_method.AuthenticationMethod"
    ]
    """<p>A structure that contains details about the requested authentication method.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationAuthenticationMethodResponse) -> dict:
    out: dict = {}
    if "authentication_method" in value:
        import capo_sso_admin.types.authentication_method

        out["AuthenticationMethod"] = (
            capo_sso_admin.types.authentication_method.serialize_aws_json_1_1(
                value["authentication_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationAuthenticationMethodResponse:
    out: GetApplicationAuthenticationMethodResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationMethod" in data:
        import capo_sso_admin.types.authentication_method

        out["authentication_method"] = (
            capo_sso_admin.types.authentication_method.deserialize_aws_json_1_1(
                data["AuthenticationMethod"]
            )
        )
    return out
