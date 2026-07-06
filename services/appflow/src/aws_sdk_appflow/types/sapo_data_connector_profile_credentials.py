"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.basic_auth_credentials
    import aws_sdk_appflow.types.o_auth_credentials


class SAPODataConnectorProfileCredentials(TypedDict, closed=True):
    basic_auth_credentials: NotRequired[
        "aws_sdk_appflow.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p> The SAPOData basic authentication credentials. </p>"""
    o_auth_credentials: NotRequired[
        "aws_sdk_appflow.types.o_auth_credentials.OAuthCredentials"
    ]
    """<p> The SAPOData OAuth type authentication credentials. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataConnectorProfileCredentials) -> dict:
    out: dict = {}
    if "basic_auth_credentials" in value:
        import aws_sdk_appflow.types.basic_auth_credentials

        out["basicAuthCredentials"] = (
            aws_sdk_appflow.types.basic_auth_credentials.serialize_json(
                value["basic_auth_credentials"]
            )
        )
    if "o_auth_credentials" in value:
        import aws_sdk_appflow.types.o_auth_credentials

        out["oAuthCredentials"] = (
            aws_sdk_appflow.types.o_auth_credentials.serialize_json(
                value["o_auth_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> SAPODataConnectorProfileCredentials:
    out: SAPODataConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "basicAuthCredentials" in data:
        import aws_sdk_appflow.types.basic_auth_credentials

        out["basic_auth_credentials"] = (
            aws_sdk_appflow.types.basic_auth_credentials.deserialize_json(
                data["basicAuthCredentials"]
            )
        )
    if "oAuthCredentials" in data:
        import aws_sdk_appflow.types.o_auth_credentials

        out["o_auth_credentials"] = (
            aws_sdk_appflow.types.o_auth_credentials.deserialize_json(
                data["oAuthCredentials"]
            )
        )
    return out
