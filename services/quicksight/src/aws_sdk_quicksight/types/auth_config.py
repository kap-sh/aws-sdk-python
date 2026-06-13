"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.authentication_metadata
    import aws_sdk_quicksight.types.connection_auth_type


class AuthConfig(TypedDict):
    authentication_type: (
        "aws_sdk_quicksight.types.connection_auth_type.ConnectionAuthType"
    )
    """<p>The type of authentication method.</p>"""
    authentication_metadata: (
        "aws_sdk_quicksight.types.authentication_metadata.AuthenticationMetadata"
    )
    """<p>The authentication metadata containing the specific configuration for the chosen authentication type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthConfig) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.connection_auth_type

    out["AuthenticationType"] = (
        aws_sdk_quicksight.types.connection_auth_type.serialize_json(
            value["authentication_type"]
        )
    )
    import aws_sdk_quicksight.types.authentication_metadata

    out["AuthenticationMetadata"] = (
        aws_sdk_quicksight.types.authentication_metadata.serialize_json(
            value["authentication_metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuthConfig:
    out: AuthConfig = {}  # type: ignore[typeddict-item]
    if "AuthenticationType" in data:
        import aws_sdk_quicksight.types.connection_auth_type

        out["authentication_type"] = (
            aws_sdk_quicksight.types.connection_auth_type.deserialize_json(
                data["AuthenticationType"]
            )
        )
    else:
        raise DeserializationError("AuthConfig.authentication_type required")
    if "AuthenticationMetadata" in data:
        import aws_sdk_quicksight.types.authentication_metadata

        out["authentication_metadata"] = (
            aws_sdk_quicksight.types.authentication_metadata.deserialize_json(
                data["AuthenticationMetadata"]
            )
        )
    else:
        raise DeserializationError("AuthConfig.authentication_metadata required")
    return out
