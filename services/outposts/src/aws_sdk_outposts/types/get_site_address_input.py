"""Generated from Smithy shape ``com.amazonaws.outposts#GetSiteAddressInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.address_type
    import aws_sdk_outposts.types.site_id


class GetSiteAddressInput(TypedDict):
    site_id: "aws_sdk_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""
    address_type: "aws_sdk_outposts.types.address_type.AddressType"
    """<p>The type of the address you request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSiteAddressInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSiteAddressInput:
    out: GetSiteAddressInput = {}  # type: ignore[typeddict-item]
    return out
