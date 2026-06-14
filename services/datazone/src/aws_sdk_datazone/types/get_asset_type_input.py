"""Generated from Smithy shape ``com.amazonaws.datazone#GetAssetTypeInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_type_identifier
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.revision


class GetAssetTypeInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the asset type exists.</p>"""
    identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier"
    """<p>The ID of the asset type.</p>"""
    revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the asset type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetTypeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetTypeInput:
    out: GetAssetTypeInput = {}  # type: ignore[typeddict-item]
    return out
