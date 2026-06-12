"""Generated from Smithy shape ``com.amazonaws.aiops#GetInvestigationGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_group_identifier


class GetInvestigationGroupRequest(TypedDict):
    identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier"
    """<p>Specify either the name or the ARN of the investigation group that you want to view. This is used to set the name of the investigation group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInvestigationGroupRequest:
    out: GetInvestigationGroupRequest = {}  # type: ignore[typeddict-item]
    return out
