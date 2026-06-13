"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteAssetInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_identifier
    import aws_sdk_datazone.types.domain_id


class DeleteAssetInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the asset is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The identifier of the asset that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetInput:
    out: DeleteAssetInput = {}  # type: ignore[typeddict-item]
    return out
