"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateManagedLoginBrandingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.managed_login_branding_type


class CreateManagedLoginBrandingResponse(TypedDict, closed=True):
    managed_login_branding: NotRequired[
        "capo_cognito_identity_provider.types.managed_login_branding_type.ManagedLoginBrandingType"
    ]
    """<p>The details of the branding style that you created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateManagedLoginBrandingResponse) -> dict:
    out: dict = {}
    if "managed_login_branding" in value:
        import capo_cognito_identity_provider.types.managed_login_branding_type

        out["ManagedLoginBranding"] = (
            capo_cognito_identity_provider.types.managed_login_branding_type.serialize_aws_json_1_1(
                value["managed_login_branding"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateManagedLoginBrandingResponse:
    out: CreateManagedLoginBrandingResponse = {}  # type: ignore[typeddict-item]
    if "ManagedLoginBranding" in data:
        import capo_cognito_identity_provider.types.managed_login_branding_type

        out["managed_login_branding"] = (
            capo_cognito_identity_provider.types.managed_login_branding_type.deserialize_aws_json_1_1(
                data["ManagedLoginBranding"]
            )
        )
    return out
