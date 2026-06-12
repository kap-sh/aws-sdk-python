"""Generated from Smithy shape ``com.amazonaws.appflow#CustomAuthConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.auth_parameter_list
    import aws_sdk_appflow.types.custom_authentication_type


class CustomAuthConfig(TypedDict):
    custom_authentication_type: NotRequired[
        "aws_sdk_appflow.types.custom_authentication_type.CustomAuthenticationType"
    ]
    """<p>The authentication type that the custom connector uses.</p>"""
    auth_parameters: NotRequired[
        "aws_sdk_appflow.types.auth_parameter_list.AuthParameterList"
    ]
    """<p>Information about authentication parameters required for authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomAuthConfig) -> dict:
    out: dict = {}
    if "custom_authentication_type" in value:
        out["customAuthenticationType"] = value["custom_authentication_type"]
    if "auth_parameters" in value:
        import aws_sdk_appflow.types.auth_parameter_list

        out["authParameters"] = (
            aws_sdk_appflow.types.auth_parameter_list.serialize_json(
                value["auth_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomAuthConfig:
    out: CustomAuthConfig = {}  # type: ignore[typeddict-item]
    if "customAuthenticationType" in data:
        out["custom_authentication_type"] = data["customAuthenticationType"]
    if "authParameters" in data:
        import aws_sdk_appflow.types.auth_parameter_list

        out["auth_parameters"] = (
            aws_sdk_appflow.types.auth_parameter_list.deserialize_json(
                data["authParameters"]
            )
        )
    return out
