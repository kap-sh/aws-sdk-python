"""Generated from Smithy shape ``com.amazonaws.outposts#GetSiteAddressOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.address
    import capo_outposts.types.address_type
    import capo_outposts.types.site_id


class GetSiteAddressOutput(TypedDict, closed=True):
    site_id: NotRequired["capo_outposts.types.site_id.SiteId"]
    address_type: NotRequired["capo_outposts.types.address_type.AddressType"]
    """<p>The type of the address you receive. </p>"""
    address: NotRequired["capo_outposts.types.address.Address"]
    """<p> Information about the address. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSiteAddressOutput) -> dict:
    out: dict = {}
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    if "address_type" in value:
        import capo_outposts.types.address_type

        out["AddressType"] = capo_outposts.types.address_type.serialize_json(
            value["address_type"]
        )
    if "address" in value:
        import capo_outposts.types.address

        out["Address"] = capo_outposts.types.address.serialize_json(value["address"])
    return out


def deserialize_json(data: dict) -> GetSiteAddressOutput:
    out: GetSiteAddressOutput = {}  # type: ignore[typeddict-item]
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    if "AddressType" in data:
        import capo_outposts.types.address_type

        out["address_type"] = capo_outposts.types.address_type.deserialize_json(
            data["AddressType"]
        )
    if "Address" in data:
        import capo_outposts.types.address

        out["address"] = capo_outposts.types.address.deserialize_json(data["Address"])
    return out
