"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateLinkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.bandwidth
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.site_id
    import aws_sdk_networkmanager.types.tag_list


class CreateLinkRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of the link.</p> <p>Constraints: Maximum length of 256 characters.</p>"""
    type: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The type of the link.</p> <p>Constraints: Maximum length of 128 characters. Cannot include the following characters: | \ ^</p>"""
    bandwidth: "aws_sdk_networkmanager.types.bandwidth.Bandwidth"
    """<p> The upload speed and download speed in Mbps. </p>"""
    provider: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The provider of the link.</p> <p>Constraints: Maximum length of 128 characters. Cannot include the following characters: | \ ^</p>"""
    site_id: "aws_sdk_networkmanager.types.site_id.SiteId"
    """<p>The ID of the site.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The tags to apply to the resource during creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    import aws_sdk_networkmanager.types.bandwidth

    out["Bandwidth"] = aws_sdk_networkmanager.types.bandwidth.serialize_json(
        value["bandwidth"]
    )
    if "provider" in value:
        out["Provider"] = value["provider"]
    out["SiteId"] = value["site_id"]
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateLinkRequest:
    out: CreateLinkRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Bandwidth" in data:
        import aws_sdk_networkmanager.types.bandwidth

        out["bandwidth"] = aws_sdk_networkmanager.types.bandwidth.deserialize_json(
            data["Bandwidth"]
        )
    else:
        raise DeserializationError("CreateLinkRequest.bandwidth required")
    if "Provider" in data:
        out["provider"] = data["Provider"]
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    else:
        raise DeserializationError("CreateLinkRequest.site_id required")
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
