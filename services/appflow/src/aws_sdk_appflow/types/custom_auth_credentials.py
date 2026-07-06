"""Generated from Smithy shape ``com.amazonaws.appflow#CustomAuthCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.credentials_map
    import aws_sdk_appflow.types.custom_authentication_type


class CustomAuthCredentials(TypedDict, closed=True):
    custom_authentication_type: (
        "aws_sdk_appflow.types.custom_authentication_type.CustomAuthenticationType"
    )
    """<p>The custom authentication type that the connector uses.</p>"""
    credentials_map: NotRequired["aws_sdk_appflow.types.credentials_map.CredentialsMap"]
    """<p>A map that holds custom authentication credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomAuthCredentials) -> dict:
    out: dict = {}
    out["customAuthenticationType"] = value["custom_authentication_type"]
    if "credentials_map" in value:
        import aws_sdk_appflow.types.credentials_map

        out["credentialsMap"] = aws_sdk_appflow.types.credentials_map.serialize_json(
            value["credentials_map"]
        )
    return out


def deserialize_json(data: dict) -> CustomAuthCredentials:
    out: CustomAuthCredentials = {}  # type: ignore[typeddict-item]
    if "customAuthenticationType" in data:
        out["custom_authentication_type"] = data["customAuthenticationType"]
    else:
        raise DeserializationError(
            "CustomAuthCredentials.custom_authentication_type required"
        )
    if "credentialsMap" in data:
        import aws_sdk_appflow.types.credentials_map

        out["credentials_map"] = aws_sdk_appflow.types.credentials_map.deserialize_json(
            data["credentialsMap"]
        )
    return out
