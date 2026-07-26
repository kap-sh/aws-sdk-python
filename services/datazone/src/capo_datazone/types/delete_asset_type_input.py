"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteAssetTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_type_identifier
    import capo_datazone.types.domain_id


class DeleteAssetTypeInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the asset type is deleted.</p>"""
    identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier"
    """<p>The identifier of the asset type that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetTypeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetTypeInput:
    out: DeleteAssetTypeInput = {}  # type: ignore[typeddict-item]
    return out
