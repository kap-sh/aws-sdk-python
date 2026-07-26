"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.pillar_metrics
    import capo_wellarchitected.types.risk_counts


class LensMetric(TypedDict, closed=True):
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>The lens ARN.</p>"""
    pillars: NotRequired["capo_wellarchitected.types.pillar_metrics.PillarMetrics"]
    """<p>The metrics for the pillars in a lens.</p>"""
    risk_counts: NotRequired["capo_wellarchitected.types.risk_counts.RiskCounts"]


# --- restJson1 ser/de ---
def serialize_json(value: LensMetric) -> dict:
    out: dict = {}
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "pillars" in value:
        import capo_wellarchitected.types.pillar_metrics

        out["Pillars"] = capo_wellarchitected.types.pillar_metrics.serialize_json(
            value["pillars"]
        )
    if "risk_counts" in value:
        import capo_wellarchitected.types.risk_counts

        out["RiskCounts"] = capo_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    return out


def deserialize_json(data: dict) -> LensMetric:
    out: LensMetric = {}  # type: ignore[typeddict-item]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "Pillars" in data:
        import capo_wellarchitected.types.pillar_metrics

        out["pillars"] = capo_wellarchitected.types.pillar_metrics.deserialize_json(
            data["Pillars"]
        )
    if "RiskCounts" in data:
        import capo_wellarchitected.types.risk_counts

        out["risk_counts"] = capo_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    return out
