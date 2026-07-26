"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUserSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.mfa_option_list_type
    import capo_cognito_identity_provider.types.token_model_type


class SetUserSettingsRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    mfa_options: (
        "capo_cognito_identity_provider.types.mfa_option_list_type.MFAOptionListType"
    )
    """<p>You can use this parameter only to set an SMS configuration that uses SMS for delivery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUserSettingsRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    import capo_cognito_identity_provider.types.mfa_option_list_type

    out["MFAOptions"] = (
        capo_cognito_identity_provider.types.mfa_option_list_type.serialize_aws_json_1_1(
            value["mfa_options"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUserSettingsRequest:
    out: SetUserSettingsRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("SetUserSettingsRequest.access_token required")
    if "MFAOptions" in data:
        import capo_cognito_identity_provider.types.mfa_option_list_type

        out["mfa_options"] = (
            capo_cognito_identity_provider.types.mfa_option_list_type.deserialize_aws_json_1_1(
                data["MFAOptions"]
            )
        )
    else:
        raise DeserializationError("SetUserSettingsRequest.mfa_options required")
    return out
