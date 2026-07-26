"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUICustomizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.ui_customization_type


class GetUICustomizationResponse(TypedDict, closed=True):
    ui_customization: (
        "capo_cognito_identity_provider.types.ui_customization_type.UICustomizationType"
    )
    """<p>Information about the classic hosted UI custom CSS and logo-image branding that you applied to the user pool or app client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUICustomizationResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.ui_customization_type

    out["UICustomization"] = (
        capo_cognito_identity_provider.types.ui_customization_type.serialize_aws_json_1_1(
            value["ui_customization"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUICustomizationResponse:
    out: GetUICustomizationResponse = {}  # type: ignore[typeddict-item]
    if "UICustomization" in data:
        import capo_cognito_identity_provider.types.ui_customization_type

        out["ui_customization"] = (
            capo_cognito_identity_provider.types.ui_customization_type.deserialize_aws_json_1_1(
                data["UICustomization"]
            )
        )
    else:
        raise DeserializationError(
            "GetUICustomizationResponse.ui_customization required"
        )
    return out
