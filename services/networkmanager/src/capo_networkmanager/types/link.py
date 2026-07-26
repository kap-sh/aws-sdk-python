"""Generated from Smithy shape ``com.amazonaws.networkmanager#Link``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.bandwidth
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_arn
    import capo_networkmanager.types.link_id
    import capo_networkmanager.types.link_state
    import capo_networkmanager.types.site_id
    import capo_networkmanager.types.tag_list


class Link(TypedDict, closed=True):
    link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""
    link_arn: NotRequired["capo_networkmanager.types.link_arn.LinkArn"]
    """<p>The Amazon Resource Name (ARN) of the link.</p>"""
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    site_id: NotRequired["capo_networkmanager.types.site_id.SiteId"]
    """<p>The ID of the site.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the link.</p>"""
    type: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The type of the link.</p>"""
    bandwidth: NotRequired["capo_networkmanager.types.bandwidth.Bandwidth"]
    """<p>The bandwidth for the link.</p>"""
    provider: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The provider of the link.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the link was created.</p>"""
    state: NotRequired["capo_networkmanager.types.link_state.LinkState"]
    """<p>The state of the link.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags for the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Link) -> dict:
    out: dict = {}
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "link_arn" in value:
        out["LinkArn"] = value["link_arn"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    if "bandwidth" in value:
        import capo_networkmanager.types.bandwidth

        out["Bandwidth"] = capo_networkmanager.types.bandwidth.serialize_json(
            value["bandwidth"]
        )
    if "provider" in value:
        out["Provider"] = value["provider"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.link_state

        out["State"] = capo_networkmanager.types.link_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Link:
    out: Link = {}  # type: ignore[typeddict-item]
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    if "LinkArn" in data:
        out["link_arn"] = data["LinkArn"]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Bandwidth" in data:
        import capo_networkmanager.types.bandwidth

        out["bandwidth"] = capo_networkmanager.types.bandwidth.deserialize_json(
            data["Bandwidth"]
        )
    if "Provider" in data:
        out["provider"] = data["Provider"]
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "State" in data:
        import capo_networkmanager.types.link_state

        out["state"] = capo_networkmanager.types.link_state.deserialize_json(
            data["State"]
        )
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out
