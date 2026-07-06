"""Generated from Smithy shape ``com.amazonaws.outposts#CreateSiteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.address
    import aws_sdk_outposts.types.rack_physical_properties
    import aws_sdk_outposts.types.site_description
    import aws_sdk_outposts.types.site_name
    import aws_sdk_outposts.types.site_notes
    import aws_sdk_outposts.types.tag_map


class CreateSiteInput(TypedDict, closed=True):
    name: "aws_sdk_outposts.types.site_name.SiteName"
    description: NotRequired["aws_sdk_outposts.types.site_description.SiteDescription"]
    notes: NotRequired["aws_sdk_outposts.types.site_notes.SiteNotes"]
    """<p>Additional information that you provide about site access requirements, electrician scheduling, personal protective equipment, or regulation of equipment materials that could affect your installation process. </p>"""
    tags: NotRequired["aws_sdk_outposts.types.tag_map.TagMap"]
    """<p> The tags to apply to a site. </p>"""
    operating_address: NotRequired["aws_sdk_outposts.types.address.Address"]
    """<p> The location to install and power on the hardware. This address might be different from the shipping address. </p>"""
    shipping_address: NotRequired["aws_sdk_outposts.types.address.Address"]
    """<p> The location to ship the hardware. This address might be different from the operating address. </p>"""
    rack_physical_properties: NotRequired[
        "aws_sdk_outposts.types.rack_physical_properties.RackPhysicalProperties"
    ]
    r"""<p> Information about the physical and logistical details for the rack at this site. For more information about hardware requirements for racks, see <a href=\"https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#checklist\">Network readiness checklist</a> in the Amazon Web Services Outposts User Guide. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSiteInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "tags" in value:
        import aws_sdk_outposts.types.tag_map

        out["Tags"] = aws_sdk_outposts.types.tag_map.serialize_json(value["tags"])
    if "operating_address" in value:
        import aws_sdk_outposts.types.address

        out["OperatingAddress"] = aws_sdk_outposts.types.address.serialize_json(
            value["operating_address"]
        )
    if "shipping_address" in value:
        import aws_sdk_outposts.types.address

        out["ShippingAddress"] = aws_sdk_outposts.types.address.serialize_json(
            value["shipping_address"]
        )
    if "rack_physical_properties" in value:
        import aws_sdk_outposts.types.rack_physical_properties

        out["RackPhysicalProperties"] = (
            aws_sdk_outposts.types.rack_physical_properties.serialize_json(
                value["rack_physical_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSiteInput:
    out: CreateSiteInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSiteInput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "Tags" in data:
        import aws_sdk_outposts.types.tag_map

        out["tags"] = aws_sdk_outposts.types.tag_map.deserialize_json(data["Tags"])
    if "OperatingAddress" in data:
        import aws_sdk_outposts.types.address

        out["operating_address"] = aws_sdk_outposts.types.address.deserialize_json(
            data["OperatingAddress"]
        )
    if "ShippingAddress" in data:
        import aws_sdk_outposts.types.address

        out["shipping_address"] = aws_sdk_outposts.types.address.deserialize_json(
            data["ShippingAddress"]
        )
    if "RackPhysicalProperties" in data:
        import aws_sdk_outposts.types.rack_physical_properties

        out["rack_physical_properties"] = (
            aws_sdk_outposts.types.rack_physical_properties.deserialize_json(
                data["RackPhysicalProperties"]
            )
        )
    return out
