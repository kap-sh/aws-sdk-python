"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteAssetFilterInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.filter_id


class DeleteAssetFilterInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to delete an asset filter.</p>"""
    asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The ID of the data asset.</p>"""
    identifier: "aws_sdk_datazone.types.filter_id.FilterId"
    """<p>The ID of the asset filter that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetFilterInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetFilterInput:
    out: DeleteAssetFilterInput = {}  # type: ignore[typeddict-item]
    return out
