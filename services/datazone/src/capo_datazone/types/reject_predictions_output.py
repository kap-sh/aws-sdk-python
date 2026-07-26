"""Generated from Smithy shape ``com.amazonaws.datazone#RejectPredictionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.domain_id
    import capo_datazone.types.revision


class RejectPredictionsOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The ID of the asset.</p>"""
    asset_revision: "capo_datazone.types.revision.Revision"
    """<p>The revision that is to be made to the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectPredictionsOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["assetId"] = value["asset_id"]
    out["assetRevision"] = value["asset_revision"]
    return out


def deserialize_json(data: dict) -> RejectPredictionsOutput:
    out: RejectPredictionsOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("RejectPredictionsOutput.domain_id required")
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("RejectPredictionsOutput.asset_id required")
    if "assetRevision" in data:
        out["asset_revision"] = data["assetRevision"]
    else:
        raise DeserializationError("RejectPredictionsOutput.asset_revision required")
    return out
