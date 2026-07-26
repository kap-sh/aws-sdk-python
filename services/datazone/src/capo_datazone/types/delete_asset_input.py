"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteAssetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_identifier
    import capo_datazone.types.domain_id


class DeleteAssetInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the asset is deleted.</p>"""
    identifier: "capo_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The identifier of the asset that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetInput:
    out: DeleteAssetInput = {}  # type: ignore[typeddict-item]
    return out
