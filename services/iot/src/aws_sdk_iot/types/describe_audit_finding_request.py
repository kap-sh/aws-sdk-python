"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditFindingRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.finding_id


class DescribeAuditFindingRequest(TypedDict):
    finding_id: "aws_sdk_iot.types.finding_id.FindingId"
    """<p>A unique identifier for a single audit finding. You can use this identifier to apply mitigation actions to the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditFindingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAuditFindingRequest:
    out: DescribeAuditFindingRequest = {}  # type: ignore[typeddict-item]
    return out
