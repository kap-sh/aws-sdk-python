"""Generated from Smithy shape ``com.amazonaws.appsync#AuthMode``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.authentication_type


class AuthMode(TypedDict):
    auth_type: "aws_sdk_appsync.types.authentication_type.AuthenticationType"
    """<p>The authorization type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthMode) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.authentication_type

    out["authType"] = aws_sdk_appsync.types.authentication_type.serialize_json(
        value["auth_type"]
    )
    return out


def deserialize_json(data: dict) -> AuthMode:
    out: AuthMode = {}  # type: ignore[typeddict-item]
    if "authType" in data:
        import aws_sdk_appsync.types.authentication_type

        out["auth_type"] = aws_sdk_appsync.types.authentication_type.deserialize_json(
            data["authType"]
        )
    else:
        raise DeserializationError("AuthMode.auth_type required")
    return out
