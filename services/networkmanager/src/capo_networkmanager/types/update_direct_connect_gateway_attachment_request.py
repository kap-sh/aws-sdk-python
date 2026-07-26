"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateDirectConnectGatewayAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.external_region_code_list


class UpdateDirectConnectGatewayAttachmentRequest(TypedDict, closed=True):
    attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the Direct Connect gateway attachment for the updated edge locations. </p>"""
    edge_locations: NotRequired[
        "capo_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    ]
    """<p>One or more edge locations to update for the Direct Connect gateway attachment. The updated array of edge locations overwrites the previous array of locations. <code>EdgeLocations</code> is only used for Direct Connect gateway attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDirectConnectGatewayAttachmentRequest) -> dict:
    out: dict = {}
    if "edge_locations" in value:
        import capo_networkmanager.types.external_region_code_list

        out["EdgeLocations"] = (
            capo_networkmanager.types.external_region_code_list.serialize_json(
                value["edge_locations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDirectConnectGatewayAttachmentRequest:
    out: UpdateDirectConnectGatewayAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "EdgeLocations" in data:
        import capo_networkmanager.types.external_region_code_list

        out["edge_locations"] = (
            capo_networkmanager.types.external_region_code_list.deserialize_json(
                data["EdgeLocations"]
            )
        )
    return out
