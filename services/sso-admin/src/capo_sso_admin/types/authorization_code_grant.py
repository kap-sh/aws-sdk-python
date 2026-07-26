"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthorizationCodeGrant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.redirect_uris


class AuthorizationCodeGrant(TypedDict, closed=True):
    redirect_uris: NotRequired["capo_sso_admin.types.redirect_uris.RedirectUris"]
    """<p>A list of URIs that are valid locations to redirect a user's browser after the user is authorized.</p> <note> <p>RedirectUris is required when the grant type is <code>authorization_code</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizationCodeGrant) -> dict:
    out: dict = {}
    if "redirect_uris" in value:
        import capo_sso_admin.types.redirect_uris

        out["RedirectUris"] = capo_sso_admin.types.redirect_uris.serialize_aws_json_1_1(
            value["redirect_uris"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthorizationCodeGrant:
    out: AuthorizationCodeGrant = {}  # type: ignore[typeddict-item]
    if "RedirectUris" in data:
        import capo_sso_admin.types.redirect_uris

        out["redirect_uris"] = (
            capo_sso_admin.types.redirect_uris.deserialize_aws_json_1_1(
                data["RedirectUris"]
            )
        )
    return out
