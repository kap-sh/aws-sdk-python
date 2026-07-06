"""Generated from Smithy shape ``com.amazonaws.aiops#DeleteInvestigationGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_group_identifier


class DeleteInvestigationGroupRequest(TypedDict, closed=True):
    identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier"
    """<p>Specify either the name or the ARN of the investigation group that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInvestigationGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInvestigationGroupRequest:
    out: DeleteInvestigationGroupRequest = {}  # type: ignore[typeddict-item]
    return out
