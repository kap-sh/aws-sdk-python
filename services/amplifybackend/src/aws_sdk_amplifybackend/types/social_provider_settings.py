"""Generated from Smithy shape ``com.amazonaws.amplifybackend#SocialProviderSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.backend_auth_apple_provider_config
    import aws_sdk_amplifybackend.types.backend_auth_social_provider_config


class SocialProviderSettings(TypedDict):
    facebook: NotRequired[
        "aws_sdk_amplifybackend.types.backend_auth_social_provider_config.BackendAuthSocialProviderConfig"
    ]
    google: NotRequired[
        "aws_sdk_amplifybackend.types.backend_auth_social_provider_config.BackendAuthSocialProviderConfig"
    ]
    login_with_amazon: NotRequired[
        "aws_sdk_amplifybackend.types.backend_auth_social_provider_config.BackendAuthSocialProviderConfig"
    ]
    sign_in_with_apple: NotRequired[
        "aws_sdk_amplifybackend.types.backend_auth_apple_provider_config.BackendAuthAppleProviderConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SocialProviderSettings) -> dict:
    out: dict = {}
    if "facebook" in value:
        import aws_sdk_amplifybackend.types.backend_auth_social_provider_config

        out["Facebook"] = (
            aws_sdk_amplifybackend.types.backend_auth_social_provider_config.serialize_json(
                value["facebook"]
            )
        )
    if "google" in value:
        import aws_sdk_amplifybackend.types.backend_auth_social_provider_config

        out["Google"] = (
            aws_sdk_amplifybackend.types.backend_auth_social_provider_config.serialize_json(
                value["google"]
            )
        )
    if "login_with_amazon" in value:
        import aws_sdk_amplifybackend.types.backend_auth_social_provider_config

        out["LoginWithAmazon"] = (
            aws_sdk_amplifybackend.types.backend_auth_social_provider_config.serialize_json(
                value["login_with_amazon"]
            )
        )
    if "sign_in_with_apple" in value:
        import aws_sdk_amplifybackend.types.backend_auth_apple_provider_config

        out["SignInWithApple"] = (
            aws_sdk_amplifybackend.types.backend_auth_apple_provider_config.serialize_json(
                value["sign_in_with_apple"]
            )
        )
    return out


def deserialize_json(data: dict) -> SocialProviderSettings:
    out: SocialProviderSettings = {}  # type: ignore[typeddict-item]
    if "Facebook" in data:
        import aws_sdk_amplifybackend.types.backend_auth_social_provider_config

        out["facebook"] = (
            aws_sdk_amplifybackend.types.backend_auth_social_provider_config.deserialize_json(
                data["Facebook"]
            )
        )
    if "Google" in data:
        import aws_sdk_amplifybackend.types.backend_auth_social_provider_config

        out["google"] = (
            aws_sdk_amplifybackend.types.backend_auth_social_provider_config.deserialize_json(
                data["Google"]
            )
        )
    if "LoginWithAmazon" in data:
        import aws_sdk_amplifybackend.types.backend_auth_social_provider_config

        out["login_with_amazon"] = (
            aws_sdk_amplifybackend.types.backend_auth_social_provider_config.deserialize_json(
                data["LoginWithAmazon"]
            )
        )
    if "SignInWithApple" in data:
        import aws_sdk_amplifybackend.types.backend_auth_apple_provider_config

        out["sign_in_with_apple"] = (
            aws_sdk_amplifybackend.types.backend_auth_apple_provider_config.deserialize_json(
                data["SignInWithApple"]
            )
        )
    return out
