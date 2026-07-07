"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.client_token
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id


class UpdateNetworkRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network to update.</p>"""
    network_name: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The new name for the network. Must be between 1 and 20 characters.</p>"""
    client_token: NotRequired["aws_sdk_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The ARN of the Amazon Web Services KMS customer managed key to use for encrypting sensitive data in the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkRequest) -> dict:
    out: dict = {}
    out["networkName"] = value["network_name"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> UpdateNetworkRequest:
    out: UpdateNetworkRequest = {}  # type: ignore[typeddict-item]
    if "networkName" in data:
        out["network_name"] = data["networkName"]
    else:
        raise DeserializationError("UpdateNetworkRequest.network_name required")
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
