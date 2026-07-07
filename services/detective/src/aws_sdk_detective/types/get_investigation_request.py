"""Generated from Smithy shape ``com.amazonaws.detective#GetInvestigationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.graph_arn
    import aws_sdk_detective.types.investigation_id


class GetInvestigationRequest(TypedDict, closed=True):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The Amazon Resource Name (ARN) of the behavior graph.</p>"""
    investigation_id: "aws_sdk_detective.types.investigation_id.InvestigationId"
    """<p>The investigation ID of the investigation report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    out["InvestigationId"] = value["investigation_id"]
    return out


def deserialize_json(data: dict) -> GetInvestigationRequest:
    out: GetInvestigationRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("GetInvestigationRequest.graph_arn required")
    if "InvestigationId" in data:
        out["investigation_id"] = data["InvestigationId"]
    else:
        raise DeserializationError("GetInvestigationRequest.investigation_id required")
    return out
