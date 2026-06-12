"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditFindingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_finding


class DescribeAuditFindingResponse(TypedDict):
    finding: NotRequired["aws_sdk_iot.types.audit_finding.AuditFinding"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditFindingResponse) -> dict:
    out: dict = {}
    if "finding" in value:
        import aws_sdk_iot.types.audit_finding

        out["finding"] = aws_sdk_iot.types.audit_finding.serialize_json(
            value["finding"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAuditFindingResponse:
    out: DescribeAuditFindingResponse = {}  # type: ignore[typeddict-item]
    if "finding" in data:
        import aws_sdk_iot.types.audit_finding

        out["finding"] = aws_sdk_iot.types.audit_finding.deserialize_json(
            data["finding"]
        )
    return out
