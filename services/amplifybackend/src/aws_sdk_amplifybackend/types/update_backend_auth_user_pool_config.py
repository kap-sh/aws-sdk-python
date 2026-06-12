"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthUserPoolConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.update_backend_auth_forgot_password_config
    import aws_sdk_amplifybackend.types.update_backend_auth_mfa_config
    import aws_sdk_amplifybackend.types.update_backend_auth_o_auth_config
    import aws_sdk_amplifybackend.types.update_backend_auth_password_policy_config
    import aws_sdk_amplifybackend.types.update_backend_auth_verification_message_config


class UpdateBackendAuthUserPoolConfig(TypedDict):
    forgot_password: NotRequired[
        "aws_sdk_amplifybackend.types.update_backend_auth_forgot_password_config.UpdateBackendAuthForgotPasswordConfig"
    ]
    """<p><b>(DEPRECATED)</b> Describes the forgot password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    mfa: NotRequired[
        "aws_sdk_amplifybackend.types.update_backend_auth_mfa_config.UpdateBackendAuthMFAConfig"
    ]
    """<p>Describes whether to apply multi-factor authentication policies for your Amazon Cognito user pool configured as a part of your Amplify project.</p>"""
    o_auth: NotRequired[
        "aws_sdk_amplifybackend.types.update_backend_auth_o_auth_config.UpdateBackendAuthOAuthConfig"
    ]
    """<p>Describes the OAuth policy and rules for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    password_policy: NotRequired[
        "aws_sdk_amplifybackend.types.update_backend_auth_password_policy_config.UpdateBackendAuthPasswordPolicyConfig"
    ]
    """<p>Describes the password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    verification_message: NotRequired[
        "aws_sdk_amplifybackend.types.update_backend_auth_verification_message_config.UpdateBackendAuthVerificationMessageConfig"
    ]
    """<p>Describes the email or SMS verification message for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthUserPoolConfig) -> dict:
    out: dict = {}
    if "forgot_password" in value:
        import aws_sdk_amplifybackend.types.update_backend_auth_forgot_password_config

        out["forgotPassword"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_forgot_password_config.serialize_json(
                value["forgot_password"]
            )
        )
    if "mfa" in value:
        import aws_sdk_amplifybackend.types.update_backend_auth_mfa_config

        out["mfa"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_mfa_config.serialize_json(
                value["mfa"]
            )
        )
    if "o_auth" in value:
        import aws_sdk_amplifybackend.types.update_backend_auth_o_auth_config

        out["oAuth"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_o_auth_config.serialize_json(
                value["o_auth"]
            )
        )
    if "password_policy" in value:
        import aws_sdk_amplifybackend.types.update_backend_auth_password_policy_config

        out["passwordPolicy"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_password_policy_config.serialize_json(
                value["password_policy"]
            )
        )
    if "verification_message" in value:
        import aws_sdk_amplifybackend.types.update_backend_auth_verification_message_config

        out["verificationMessage"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_verification_message_config.serialize_json(
                value["verification_message"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthUserPoolConfig:
    out: UpdateBackendAuthUserPoolConfig = {}  # type: ignore[typeddict-item]
    if "forgotPassword" in data:
        import aws_sdk_amplifybackend.types.update_backend_auth_forgot_password_config

        out["forgot_password"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_forgot_password_config.deserialize_json(
                data["forgotPassword"]
            )
        )
    if "mfa" in data:
        import aws_sdk_amplifybackend.types.update_backend_auth_mfa_config

        out["mfa"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_mfa_config.deserialize_json(
                data["mfa"]
            )
        )
    if "oAuth" in data:
        import aws_sdk_amplifybackend.types.update_backend_auth_o_auth_config

        out["o_auth"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_o_auth_config.deserialize_json(
                data["oAuth"]
            )
        )
    if "passwordPolicy" in data:
        import aws_sdk_amplifybackend.types.update_backend_auth_password_policy_config

        out["password_policy"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_password_policy_config.deserialize_json(
                data["passwordPolicy"]
            )
        )
    if "verificationMessage" in data:
        import aws_sdk_amplifybackend.types.update_backend_auth_verification_message_config

        out["verification_message"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_verification_message_config.deserialize_json(
                data["verificationMessage"]
            )
        )
    return out
