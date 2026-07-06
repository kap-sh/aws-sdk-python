"""Generated from Smithy shape ``com.amazonaws.datazone#GetAssetFilterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.filter_id


class GetAssetFilterInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to get an asset filter.</p>"""
    asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The ID of the data asset.</p>"""
    identifier: "aws_sdk_datazone.types.filter_id.FilterId"
    """<p>The ID of the asset filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetFilterInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetFilterInput:
    out: GetAssetFilterInput = {}  # type: ignore[typeddict-item]
    return out
