"""Generated from Smithy shape ``com.amazonaws.datazone#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.authentication_type
    import aws_sdk_datazone.types.o_auth2_properties


class AuthenticationConfiguration(TypedDict):
    authentication_type: NotRequired[
        "aws_sdk_datazone.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type of a connection.</p>"""
    secret_arn: NotRequired["str"]
    """<p>The secret ARN of a connection.</p>"""
    o_auth2_properties: NotRequired[
        "aws_sdk_datazone.types.o_auth2_properties.OAuth2Properties"
    ]
    """<p>The oAuth2 properties of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import aws_sdk_datazone.types.authentication_type

        out["authenticationType"] = (
            aws_sdk_datazone.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    if "o_auth2_properties" in value:
        import aws_sdk_datazone.types.o_auth2_properties

        out["oAuth2Properties"] = (
            aws_sdk_datazone.types.o_auth2_properties.serialize_json(
                value["o_auth2_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "authenticationType" in data:
        import aws_sdk_datazone.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_datazone.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    if "oAuth2Properties" in data:
        import aws_sdk_datazone.types.o_auth2_properties

        out["o_auth2_properties"] = (
            aws_sdk_datazone.types.o_auth2_properties.deserialize_json(
                data["oAuth2Properties"]
            )
        )
    return out
