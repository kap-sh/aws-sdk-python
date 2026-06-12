"""Generated from Smithy shape ``com.amazonaws.outposts#Site``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.account_id
    import aws_sdk_outposts.types.city
    import aws_sdk_outposts.types.country_code
    import aws_sdk_outposts.types.rack_physical_properties
    import aws_sdk_outposts.types.site_arn
    import aws_sdk_outposts.types.site_description
    import aws_sdk_outposts.types.site_id
    import aws_sdk_outposts.types.site_name
    import aws_sdk_outposts.types.site_notes
    import aws_sdk_outposts.types.state_or_region
    import aws_sdk_outposts.types.tag_map


class Site(TypedDict):
    site_id: NotRequired["aws_sdk_outposts.types.site_id.SiteId"]
    account_id: NotRequired["aws_sdk_outposts.types.account_id.AccountId"]
    name: NotRequired["aws_sdk_outposts.types.site_name.SiteName"]
    description: NotRequired["aws_sdk_outposts.types.site_description.SiteDescription"]
    tags: NotRequired["aws_sdk_outposts.types.tag_map.TagMap"]
    """<p>The site tags.</p>"""
    site_arn: NotRequired["aws_sdk_outposts.types.site_arn.SiteArn"]
    notes: NotRequired["aws_sdk_outposts.types.site_notes.SiteNotes"]
    """<p> Notes about a site. </p>"""
    operating_address_country_code: NotRequired[
        "aws_sdk_outposts.types.country_code.CountryCode"
    ]
    """<p> The ISO-3166 two-letter country code where the hardware is installed and powered on. </p>"""
    operating_address_state_or_region: NotRequired[
        "aws_sdk_outposts.types.state_or_region.StateOrRegion"
    ]
    """<p> State or region where the hardware is installed and powered on. </p>"""
    operating_address_city: NotRequired["aws_sdk_outposts.types.city.City"]
    """<p> City where the hardware is installed and powered on. </p>"""
    rack_physical_properties: NotRequired[
        "aws_sdk_outposts.types.rack_physical_properties.RackPhysicalProperties"
    ]
    """<p> Information about the physical and logistical details for a rack at the site. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Site) -> dict:
    out: dict = {}
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_outposts.types.tag_map

        out["Tags"] = aws_sdk_outposts.types.tag_map.serialize_json(value["tags"])
    if "site_arn" in value:
        out["SiteArn"] = value["site_arn"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "operating_address_country_code" in value:
        out["OperatingAddressCountryCode"] = value["operating_address_country_code"]
    if "operating_address_state_or_region" in value:
        out["OperatingAddressStateOrRegion"] = value[
            "operating_address_state_or_region"
        ]
    if "operating_address_city" in value:
        out["OperatingAddressCity"] = value["operating_address_city"]
    if "rack_physical_properties" in value:
        import aws_sdk_outposts.types.rack_physical_properties

        out["RackPhysicalProperties"] = (
            aws_sdk_outposts.types.rack_physical_properties.serialize_json(
                value["rack_physical_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> Site:
    out: Site = {}  # type: ignore[typeddict-item]
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_outposts.types.tag_map

        out["tags"] = aws_sdk_outposts.types.tag_map.deserialize_json(data["Tags"])
    if "SiteArn" in data:
        out["site_arn"] = data["SiteArn"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "OperatingAddressCountryCode" in data:
        out["operating_address_country_code"] = data["OperatingAddressCountryCode"]
    if "OperatingAddressStateOrRegion" in data:
        out["operating_address_state_or_region"] = data["OperatingAddressStateOrRegion"]
    if "OperatingAddressCity" in data:
        out["operating_address_city"] = data["OperatingAddressCity"]
    if "RackPhysicalProperties" in data:
        import aws_sdk_outposts.types.rack_physical_properties

        out["rack_physical_properties"] = (
            aws_sdk_outposts.types.rack_physical_properties.deserialize_json(
                data["RackPhysicalProperties"]
            )
        )
    return out
