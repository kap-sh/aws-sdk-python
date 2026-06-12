"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateSiteAddressOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.address
    import aws_sdk_outposts.types.address_type


class UpdateSiteAddressOutput(TypedDict):
    address_type: NotRequired["aws_sdk_outposts.types.address_type.AddressType"]
    """<p> The type of the address. </p>"""
    address: NotRequired["aws_sdk_outposts.types.address.Address"]
    """<p> Information about an address. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteAddressOutput) -> dict:
    out: dict = {}
    if "address_type" in value:
        import aws_sdk_outposts.types.address_type

        out["AddressType"] = aws_sdk_outposts.types.address_type.serialize_json(
            value["address_type"]
        )
    if "address" in value:
        import aws_sdk_outposts.types.address

        out["Address"] = aws_sdk_outposts.types.address.serialize_json(value["address"])
    return out


def deserialize_json(data: dict) -> UpdateSiteAddressOutput:
    out: UpdateSiteAddressOutput = {}  # type: ignore[typeddict-item]
    if "AddressType" in data:
        import aws_sdk_outposts.types.address_type

        out["address_type"] = aws_sdk_outposts.types.address_type.deserialize_json(
            data["AddressType"]
        )
    if "Address" in data:
        import aws_sdk_outposts.types.address

        out["address"] = aws_sdk_outposts.types.address.deserialize_json(
            data["Address"]
        )
    return out
