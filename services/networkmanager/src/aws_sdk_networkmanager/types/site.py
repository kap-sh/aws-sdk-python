"""Generated from Smithy shape ``com.amazonaws.networkmanager#Site``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.date_time
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.location
    import aws_sdk_networkmanager.types.site_arn
    import aws_sdk_networkmanager.types.site_id
    import aws_sdk_networkmanager.types.site_state
    import aws_sdk_networkmanager.types.tag_list


class Site(TypedDict):
    site_id: NotRequired["aws_sdk_networkmanager.types.site_id.SiteId"]
    """<p>The ID of the site.</p>"""
    site_arn: NotRequired["aws_sdk_networkmanager.types.site_arn.SiteArn"]
    """<p>The Amazon Resource Name (ARN) of the site.</p>"""
    global_network_id: NotRequired[
        "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the site.</p>"""
    location: NotRequired["aws_sdk_networkmanager.types.location.Location"]
    """<p>The location of the site.</p>"""
    created_at: NotRequired["aws_sdk_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the site was created.</p>"""
    state: NotRequired["aws_sdk_networkmanager.types.site_state.SiteState"]
    """<p>The state of the site.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The tags for the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Site) -> dict:
    out: dict = {}
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    if "site_arn" in value:
        out["SiteArn"] = value["site_arn"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "location" in value:
        import aws_sdk_networkmanager.types.location

        out["Location"] = aws_sdk_networkmanager.types.location.serialize_json(
            value["location"]
        )
    if "created_at" in value:
        import aws_sdk_networkmanager.types.date_time

        out["CreatedAt"] = aws_sdk_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import aws_sdk_networkmanager.types.site_state

        out["State"] = aws_sdk_networkmanager.types.site_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> Site:
    out: Site = {}  # type: ignore[typeddict-item]
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    if "SiteArn" in data:
        out["site_arn"] = data["SiteArn"]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Location" in data:
        import aws_sdk_networkmanager.types.location

        out["location"] = aws_sdk_networkmanager.types.location.deserialize_json(
            data["Location"]
        )
    if "CreatedAt" in data:
        import aws_sdk_networkmanager.types.date_time

        out["created_at"] = aws_sdk_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "State" in data:
        import aws_sdk_networkmanager.types.site_state

        out["state"] = aws_sdk_networkmanager.types.site_state.deserialize_json(
            data["State"]
        )
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
