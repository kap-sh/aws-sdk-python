"""Generated from Smithy shape ``com.amazonaws.appflow#CustomAuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.auth_parameter_list
    import capo_appflow.types.custom_authentication_type


class CustomAuthConfig(TypedDict, closed=True):
    custom_authentication_type: NotRequired[
        "capo_appflow.types.custom_authentication_type.CustomAuthenticationType"
    ]
    """<p>The authentication type that the custom connector uses.</p>"""
    auth_parameters: NotRequired[
        "capo_appflow.types.auth_parameter_list.AuthParameterList"
    ]
    """<p>Information about authentication parameters required for authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomAuthConfig) -> dict:
    out: dict = {}
    if "custom_authentication_type" in value:
        out["customAuthenticationType"] = value["custom_authentication_type"]
    if "auth_parameters" in value:
        import capo_appflow.types.auth_parameter_list

        out["authParameters"] = capo_appflow.types.auth_parameter_list.serialize_json(
            value["auth_parameters"]
        )
    return out


def deserialize_json(data: dict) -> CustomAuthConfig:
    out: CustomAuthConfig = {}  # type: ignore[typeddict-item]
    if "customAuthenticationType" in data:
        out["custom_authentication_type"] = data["customAuthenticationType"]
    if "authParameters" in data:
        import capo_appflow.types.auth_parameter_list

        out["auth_parameters"] = (
            capo_appflow.types.auth_parameter_list.deserialize_json(
                data["authParameters"]
            )
        )
    return out
