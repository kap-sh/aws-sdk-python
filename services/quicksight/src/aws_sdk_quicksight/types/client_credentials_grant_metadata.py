"""Generated from Smithy shape ``com.amazonaws.quicksight#ClientCredentialsGrantMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.client_credentials_details
    import aws_sdk_quicksight.types.client_credentials_source
    import aws_sdk_quicksight.types.endpoint


class ClientCredentialsGrantMetadata(TypedDict):
    base_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for the external service.</p>"""
    client_credentials_source: NotRequired[
        "aws_sdk_quicksight.types.client_credentials_source.ClientCredentialsSource"
    ]
    """<p>The source of the client credentials configuration.</p>"""
    client_credentials_details: NotRequired[
        "aws_sdk_quicksight.types.client_credentials_details.ClientCredentialsDetails"
    ]
    """<p>The detailed client credentials configuration including client ID, client secret, and token endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientCredentialsGrantMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    if "client_credentials_source" in value:
        import aws_sdk_quicksight.types.client_credentials_source

        out["ClientCredentialsSource"] = (
            aws_sdk_quicksight.types.client_credentials_source.serialize_json(
                value["client_credentials_source"]
            )
        )
    if "client_credentials_details" in value:
        import aws_sdk_quicksight.types.client_credentials_details

        out["ClientCredentialsDetails"] = (
            aws_sdk_quicksight.types.client_credentials_details.serialize_json(
                value["client_credentials_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClientCredentialsGrantMetadata:
    out: ClientCredentialsGrantMetadata = {}  # type: ignore[typeddict-item]
    if "BaseEndpoint" in data:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError(
            "ClientCredentialsGrantMetadata.base_endpoint required"
        )
    if "ClientCredentialsSource" in data:
        import aws_sdk_quicksight.types.client_credentials_source

        out["client_credentials_source"] = (
            aws_sdk_quicksight.types.client_credentials_source.deserialize_json(
                data["ClientCredentialsSource"]
            )
        )
    if "ClientCredentialsDetails" in data:
        import aws_sdk_quicksight.types.client_credentials_details

        out["client_credentials_details"] = (
            aws_sdk_quicksight.types.client_credentials_details.deserialize_json(
                data["ClientCredentialsDetails"]
            )
        )
    return out
