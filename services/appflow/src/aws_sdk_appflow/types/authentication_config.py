"""Generated from Smithy shape ``com.amazonaws.appflow#AuthenticationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.custom_auth_config_list
    import aws_sdk_appflow.types.o_auth2_defaults


class AuthenticationConfig(TypedDict, closed=True):
    is_basic_auth_supported: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether basic authentication is supported by the connector.</p>"""
    is_api_key_auth_supported: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether API key authentication is supported by the connector</p>"""
    is_o_auth2_supported: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether OAuth 2.0 authentication is supported by the connector.</p>"""
    is_custom_auth_supported: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether custom authentication is supported by the connector</p>"""
    o_auth2_defaults: NotRequired[
        "aws_sdk_appflow.types.o_auth2_defaults.OAuth2Defaults"
    ]
    """<p>Contains the default values required for OAuth 2.0 authentication.</p>"""
    custom_auth_configs: NotRequired[
        "aws_sdk_appflow.types.custom_auth_config_list.CustomAuthConfigList"
    ]
    """<p>Contains information required for custom authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationConfig) -> dict:
    out: dict = {}
    out["isBasicAuthSupported"] = value.get("is_basic_auth_supported", False)
    out["isApiKeyAuthSupported"] = value.get("is_api_key_auth_supported", False)
    out["isOAuth2Supported"] = value.get("is_o_auth2_supported", False)
    out["isCustomAuthSupported"] = value.get("is_custom_auth_supported", False)
    if "o_auth2_defaults" in value:
        import aws_sdk_appflow.types.o_auth2_defaults

        out["oAuth2Defaults"] = aws_sdk_appflow.types.o_auth2_defaults.serialize_json(
            value["o_auth2_defaults"]
        )
    if "custom_auth_configs" in value:
        import aws_sdk_appflow.types.custom_auth_config_list

        out["customAuthConfigs"] = (
            aws_sdk_appflow.types.custom_auth_config_list.serialize_json(
                value["custom_auth_configs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthenticationConfig:
    out: AuthenticationConfig = {}  # type: ignore[typeddict-item]
    if "isBasicAuthSupported" in data:
        out["is_basic_auth_supported"] = data["isBasicAuthSupported"]
    else:
        out["is_basic_auth_supported"] = False
    if "isApiKeyAuthSupported" in data:
        out["is_api_key_auth_supported"] = data["isApiKeyAuthSupported"]
    else:
        out["is_api_key_auth_supported"] = False
    if "isOAuth2Supported" in data:
        out["is_o_auth2_supported"] = data["isOAuth2Supported"]
    else:
        out["is_o_auth2_supported"] = False
    if "isCustomAuthSupported" in data:
        out["is_custom_auth_supported"] = data["isCustomAuthSupported"]
    else:
        out["is_custom_auth_supported"] = False
    if "oAuth2Defaults" in data:
        import aws_sdk_appflow.types.o_auth2_defaults

        out["o_auth2_defaults"] = (
            aws_sdk_appflow.types.o_auth2_defaults.deserialize_json(
                data["oAuth2Defaults"]
            )
        )
    if "customAuthConfigs" in data:
        import aws_sdk_appflow.types.custom_auth_config_list

        out["custom_auth_configs"] = (
            aws_sdk_appflow.types.custom_auth_config_list.deserialize_json(
                data["customAuthConfigs"]
            )
        )
    return out
