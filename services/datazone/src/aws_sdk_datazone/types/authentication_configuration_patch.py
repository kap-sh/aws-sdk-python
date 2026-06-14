"""Generated from Smithy shape ``com.amazonaws.datazone#AuthenticationConfigurationPatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.basic_authentication_credentials


class AuthenticationConfigurationPatch(TypedDict):
    secret_arn: NotRequired["str"]
    """<p>The secret ARN of a connection.</p>"""
    basic_authentication_credentials: NotRequired[
        "aws_sdk_datazone.types.basic_authentication_credentials.BasicAuthenticationCredentials"
    ]
    """<p>The basic authentication credentials of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationConfigurationPatch) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    if "basic_authentication_credentials" in value:
        import aws_sdk_datazone.types.basic_authentication_credentials

        out["basicAuthenticationCredentials"] = (
            aws_sdk_datazone.types.basic_authentication_credentials.serialize_json(
                value["basic_authentication_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthenticationConfigurationPatch:
    out: AuthenticationConfigurationPatch = {}  # type: ignore[typeddict-item]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    if "basicAuthenticationCredentials" in data:
        import aws_sdk_datazone.types.basic_authentication_credentials

        out["basic_authentication_credentials"] = (
            aws_sdk_datazone.types.basic_authentication_credentials.deserialize_json(
                data["basicAuthenticationCredentials"]
            )
        )
    return out
