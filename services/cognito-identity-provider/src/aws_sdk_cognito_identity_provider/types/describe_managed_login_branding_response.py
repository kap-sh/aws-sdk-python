"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeManagedLoginBrandingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.managed_login_branding_type


class DescribeManagedLoginBrandingResponse(TypedDict, closed=True):
    managed_login_branding: NotRequired[
        "aws_sdk_cognito_identity_provider.types.managed_login_branding_type.ManagedLoginBrandingType"
    ]
    """<p>The details of the requested branding style.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeManagedLoginBrandingResponse) -> dict:
    out: dict = {}
    if "managed_login_branding" in value:
        import aws_sdk_cognito_identity_provider.types.managed_login_branding_type

        out["ManagedLoginBranding"] = (
            aws_sdk_cognito_identity_provider.types.managed_login_branding_type.serialize_aws_json_1_1(
                value["managed_login_branding"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeManagedLoginBrandingResponse:
    out: DescribeManagedLoginBrandingResponse = {}  # type: ignore[typeddict-item]
    if "ManagedLoginBranding" in data:
        import aws_sdk_cognito_identity_provider.types.managed_login_branding_type

        out["managed_login_branding"] = (
            aws_sdk_cognito_identity_provider.types.managed_login_branding_type.deserialize_aws_json_1_1(
                data["ManagedLoginBranding"]
            )
        )
    return out
