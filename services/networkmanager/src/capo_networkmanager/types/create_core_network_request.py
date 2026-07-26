"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateCoreNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_policy_document
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.tag_list


class CreateCoreNetworkRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network that a core network will be a part of. </p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of a core network.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>Key-value tags associated with a core network request.</p>"""
    policy_document: NotRequired[
        "capo_networkmanager.types.core_network_policy_document.CoreNetworkPolicyDocument"
    ]
    """<p>The policy document for creating a core network.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with a core network request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCoreNetworkRequest) -> dict:
    out: dict = {}
    out["GlobalNetworkId"] = value["global_network_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "policy_document" in value:
        out["PolicyDocument"] = value["policy_document"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCoreNetworkRequest:
    out: CreateCoreNetworkRequest = {}  # type: ignore[typeddict-item]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    else:
        raise DeserializationError(
            "CreateCoreNetworkRequest.global_network_id required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if "PolicyDocument" in data:
        out["policy_document"] = data["PolicyDocument"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
