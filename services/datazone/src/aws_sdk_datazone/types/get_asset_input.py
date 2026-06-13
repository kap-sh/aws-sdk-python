"""Generated from Smithy shape ``com.amazonaws.datazone#GetAssetInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_identifier
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.revision


class GetAssetInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain to which the asset belongs.</p>"""
    identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The ID of the Amazon DataZone asset.</p> <p>This parameter supports either the value of <code>assetId</code> or <code>externalIdentifier</code> as input. If you are passing the value of <code>externalIdentifier</code>, you must prefix this value with <code>externalIdentifer%2F</code>.</p>"""
    revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the Amazon DataZone asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetInput:
    out: GetAssetInput = {}  # type: ignore[typeddict-item]
    return out
