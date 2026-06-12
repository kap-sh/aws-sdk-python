"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociatedCoreNetwork``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.core_network_attachment_id
    import aws_sdk_direct_connect.types.core_network_identifier
    import aws_sdk_direct_connect.types.owner_account


class AssociatedCoreNetwork(TypedDict):
    id: NotRequired[
        "aws_sdk_direct_connect.types.core_network_identifier.CoreNetworkIdentifier"
    ]
    """<p>The ID of the Cloud WAN core network that the Direct Connect gateway is associated to.</p>"""
    owner_account: NotRequired[
        "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The account owner of the Cloud WAN core network.</p>"""
    attachment_id: NotRequired[
        "aws_sdk_direct_connect.types.core_network_attachment_id.CoreNetworkAttachmentId"
    ]
    """<p>the ID of the Direct Connect gateway attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedCoreNetwork) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatedCoreNetwork:
    out: AssociatedCoreNetwork = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "attachmentId" in data:
        out["attachment_id"] = data["attachmentId"]
    return out
