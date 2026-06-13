"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadClientCredentialsGrantMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.client_credentials_source
    import aws_sdk_quicksight.types.endpoint
    import aws_sdk_quicksight.types.read_client_credentials_details


class ReadClientCredentialsGrantMetadata(TypedDict):
    base_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for the OAuth2 client credentials grant flow.</p>"""
    read_client_credentials_details: NotRequired[
        "aws_sdk_quicksight.types.read_client_credentials_details.ReadClientCredentialsDetails"
    ]
    """<p>The read-only client credentials configuration details.</p>"""
    client_credentials_source: NotRequired[
        "aws_sdk_quicksight.types.client_credentials_source.ClientCredentialsSource"
    ]
    """<p>The source of client credentials for the OAuth2 client credentials grant flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadClientCredentialsGrantMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    if "read_client_credentials_details" in value:
        import aws_sdk_quicksight.types.read_client_credentials_details

        out["ReadClientCredentialsDetails"] = (
            aws_sdk_quicksight.types.read_client_credentials_details.serialize_json(
                value["read_client_credentials_details"]
            )
        )
    if "client_credentials_source" in value:
        import aws_sdk_quicksight.types.client_credentials_source

        out["ClientCredentialsSource"] = (
            aws_sdk_quicksight.types.client_credentials_source.serialize_json(
                value["client_credentials_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReadClientCredentialsGrantMetadata:
    out: ReadClientCredentialsGrantMetadata = {}  # type: ignore[typeddict-item]
    if "BaseEndpoint" in data:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError(
            "ReadClientCredentialsGrantMetadata.base_endpoint required"
        )
    if "ReadClientCredentialsDetails" in data:
        import aws_sdk_quicksight.types.read_client_credentials_details

        out["read_client_credentials_details"] = (
            aws_sdk_quicksight.types.read_client_credentials_details.deserialize_json(
                data["ReadClientCredentialsDetails"]
            )
        )
    if "ClientCredentialsSource" in data:
        import aws_sdk_quicksight.types.client_credentials_source

        out["client_credentials_source"] = (
            aws_sdk_quicksight.types.client_credentials_source.deserialize_json(
                data["ClientCredentialsSource"]
            )
        )
    return out
