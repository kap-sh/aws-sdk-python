"""Generated from Smithy shape ``com.amazonaws.wickr#CreateNetworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id


class CreateNetworkResponse(TypedDict, closed=True):
    network_id: NotRequired["capo_wickr.types.network_id.NetworkId"]
    """<p>The unique identifier assigned to the newly created network.</p>"""
    network_name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The name of the newly created network.</p>"""
    encryption_key_arn: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The ARN of the KMS key being used to encrypt sensitive data in the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkResponse) -> dict:
    out: dict = {}
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "network_name" in value:
        out["networkName"] = value["network_name"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateNetworkResponse:
    out: CreateNetworkResponse = {}  # type: ignore[typeddict-item]
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    if "networkName" in data:
        out["network_name"] = data["networkName"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
