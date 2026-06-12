"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateSiteAddressInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.address
    import aws_sdk_outposts.types.address_type
    import aws_sdk_outposts.types.site_id


class UpdateSiteAddressInput(TypedDict):
    site_id: "aws_sdk_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""
    address_type: "aws_sdk_outposts.types.address_type.AddressType"
    """<p> The type of the address. </p>"""
    address: "aws_sdk_outposts.types.address.Address"
    """<p> The address for the site. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteAddressInput) -> dict:
    out: dict = {}
    import aws_sdk_outposts.types.address_type

    out["AddressType"] = aws_sdk_outposts.types.address_type.serialize_json(
        value["address_type"]
    )
    import aws_sdk_outposts.types.address

    out["Address"] = aws_sdk_outposts.types.address.serialize_json(value["address"])
    return out


def deserialize_json(data: dict) -> UpdateSiteAddressInput:
    out: UpdateSiteAddressInput = {}  # type: ignore[typeddict-item]
    if "AddressType" in data:
        import aws_sdk_outposts.types.address_type

        out["address_type"] = aws_sdk_outposts.types.address_type.deserialize_json(
            data["AddressType"]
        )
    else:
        raise DeserializationError("UpdateSiteAddressInput.address_type required")
    if "Address" in data:
        import aws_sdk_outposts.types.address

        out["address"] = aws_sdk_outposts.types.address.deserialize_json(
            data["Address"]
        )
    else:
        raise DeserializationError("UpdateSiteAddressInput.address required")
    return out
