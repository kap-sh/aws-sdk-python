"""Generated from Smithy shape ``com.amazonaws.appflow#ServiceNowConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.o_auth2_credentials
    import capo_appflow.types.password
    import capo_appflow.types.username


class ServiceNowConnectorProfileCredentials(TypedDict, closed=True):
    username: NotRequired["capo_appflow.types.username.Username"]
    """<p> The name of the user. </p>"""
    password: NotRequired["capo_appflow.types.password.Password"]
    """<p> The password that corresponds to the user name. </p>"""
    o_auth2_credentials: NotRequired[
        "capo_appflow.types.o_auth2_credentials.OAuth2Credentials"
    ]
    """<p> The OAuth 2.0 credentials required to authenticate the user. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowConnectorProfileCredentials) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "password" in value:
        out["password"] = value["password"]
    if "o_auth2_credentials" in value:
        import capo_appflow.types.o_auth2_credentials

        out["oAuth2Credentials"] = (
            capo_appflow.types.o_auth2_credentials.serialize_json(
                value["o_auth2_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceNowConnectorProfileCredentials:
    out: ServiceNowConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    if "password" in data:
        out["password"] = data["password"]
    if "oAuth2Credentials" in data:
        import capo_appflow.types.o_auth2_credentials

        out["o_auth2_credentials"] = (
            capo_appflow.types.o_auth2_credentials.deserialize_json(
                data["oAuth2Credentials"]
            )
        )
    return out
