"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarReviewSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.pillar_name
    import aws_sdk_wellarchitected.types.risk_counts


class PillarReviewSummary(TypedDict):
    pillar_id: NotRequired["aws_sdk_wellarchitected.types.pillar_id.PillarId"]
    pillar_name: NotRequired["aws_sdk_wellarchitected.types.pillar_name.PillarName"]
    notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    risk_counts: NotRequired["aws_sdk_wellarchitected.types.risk_counts.RiskCounts"]
    prioritized_risk_counts: NotRequired[
        "aws_sdk_wellarchitected.types.risk_counts.RiskCounts"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PillarReviewSummary) -> dict:
    out: dict = {}
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "pillar_name" in value:
        out["PillarName"] = value["pillar_name"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "risk_counts" in value:
        import aws_sdk_wellarchitected.types.risk_counts

        out["RiskCounts"] = aws_sdk_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    if "prioritized_risk_counts" in value:
        import aws_sdk_wellarchitected.types.risk_counts

        out["PrioritizedRiskCounts"] = (
            aws_sdk_wellarchitected.types.risk_counts.serialize_json(
                value["prioritized_risk_counts"]
            )
        )
    return out


def deserialize_json(data: dict) -> PillarReviewSummary:
    out: PillarReviewSummary = {}  # type: ignore[typeddict-item]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "PillarName" in data:
        out["pillar_name"] = data["PillarName"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "RiskCounts" in data:
        import aws_sdk_wellarchitected.types.risk_counts

        out["risk_counts"] = aws_sdk_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    if "PrioritizedRiskCounts" in data:
        import aws_sdk_wellarchitected.types.risk_counts

        out["prioritized_risk_counts"] = (
            aws_sdk_wellarchitected.types.risk_counts.deserialize_json(
                data["PrioritizedRiskCounts"]
            )
        )
    return out
