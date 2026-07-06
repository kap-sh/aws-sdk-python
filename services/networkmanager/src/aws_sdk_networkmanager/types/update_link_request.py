"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.bandwidth
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.link_id


class UpdateLinkRequest(TypedDict, closed=True):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    link_id: "aws_sdk_networkmanager.types.link_id.LinkId"
    """<p>The ID of the link.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of the link.</p> <p>Constraints: Maximum length of 256 characters.</p>"""
    type: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The type of the link.</p> <p>Constraints: Maximum length of 128 characters.</p>"""
    bandwidth: NotRequired["aws_sdk_networkmanager.types.bandwidth.Bandwidth"]
    """<p>The upload and download speed in Mbps. </p>"""
    provider: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The provider of the link.</p> <p>Constraints: Maximum length of 128 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    if "bandwidth" in value:
        import aws_sdk_networkmanager.types.bandwidth

        out["Bandwidth"] = aws_sdk_networkmanager.types.bandwidth.serialize_json(
            value["bandwidth"]
        )
    if "provider" in value:
        out["Provider"] = value["provider"]
    return out


def deserialize_json(data: dict) -> UpdateLinkRequest:
    out: UpdateLinkRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Bandwidth" in data:
        import aws_sdk_networkmanager.types.bandwidth

        out["bandwidth"] = aws_sdk_networkmanager.types.bandwidth.deserialize_json(
            data["Bandwidth"]
        )
    if "Provider" in data:
        out["provider"] = data["Provider"]
    return out
