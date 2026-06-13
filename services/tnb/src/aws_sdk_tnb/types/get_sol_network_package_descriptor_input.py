"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageDescriptorInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.nsd_info_id


class GetSolNetworkPackageDescriptorInput(TypedDict):
    nsd_info_id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageDescriptorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageDescriptorInput:
    out: GetSolNetworkPackageDescriptorInput = {}  # type: ignore[typeddict-item]
    return out
