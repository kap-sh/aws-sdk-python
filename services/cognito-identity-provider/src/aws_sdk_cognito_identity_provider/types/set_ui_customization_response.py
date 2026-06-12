"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUICustomizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.ui_customization_type


class SetUICustomizationResponse(TypedDict):
    ui_customization: "aws_sdk_cognito_identity_provider.types.ui_customization_type.UICustomizationType"
    """<p>Information about the hosted UI branding that you applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUICustomizationResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.ui_customization_type

    out["UICustomization"] = (
        aws_sdk_cognito_identity_provider.types.ui_customization_type.serialize_aws_json_1_1(
            value["ui_customization"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUICustomizationResponse:
    out: SetUICustomizationResponse = {}  # type: ignore[typeddict-item]
    if "UICustomization" in data:
        import aws_sdk_cognito_identity_provider.types.ui_customization_type

        out["ui_customization"] = (
            aws_sdk_cognito_identity_provider.types.ui_customization_type.deserialize_aws_json_1_1(
                data["UICustomization"]
            )
        )
    else:
        raise DeserializationError(
            "SetUICustomizationResponse.ui_customization required"
        )
    return out
