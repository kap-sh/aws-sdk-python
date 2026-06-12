"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptPredictionsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.revision

class AcceptPredictionsOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    asset_id: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The ID of the asset.</p>"""
    revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision that is to be made to the asset.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AcceptPredictionsOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["assetId"] = value["asset_id"]
    out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> AcceptPredictionsOutput:
    out: AcceptPredictionsOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("AcceptPredictionsOutput.domain_id required")
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AcceptPredictionsOutput.asset_id required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("AcceptPredictionsOutput.revision required")
    return out