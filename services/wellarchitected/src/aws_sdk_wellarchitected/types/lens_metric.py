"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.pillar_metrics
    import aws_sdk_wellarchitected.types.risk_counts


class LensMetric(TypedDict):
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The lens ARN.</p>"""
    pillars: NotRequired["aws_sdk_wellarchitected.types.pillar_metrics.PillarMetrics"]
    """<p>The metrics for the pillars in a lens.</p>"""
    risk_counts: NotRequired["aws_sdk_wellarchitected.types.risk_counts.RiskCounts"]


# --- restJson1 ser/de ---
def serialize_json(value: LensMetric) -> dict:
    out: dict = {}
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "pillars" in value:
        import aws_sdk_wellarchitected.types.pillar_metrics

        out["Pillars"] = aws_sdk_wellarchitected.types.pillar_metrics.serialize_json(
            value["pillars"]
        )
    if "risk_counts" in value:
        import aws_sdk_wellarchitected.types.risk_counts

        out["RiskCounts"] = aws_sdk_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    return out


def deserialize_json(data: dict) -> LensMetric:
    out: LensMetric = {}  # type: ignore[typeddict-item]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "Pillars" in data:
        import aws_sdk_wellarchitected.types.pillar_metrics

        out["pillars"] = aws_sdk_wellarchitected.types.pillar_metrics.deserialize_json(
            data["Pillars"]
        )
    if "RiskCounts" in data:
        import aws_sdk_wellarchitected.types.risk_counts

        out["risk_counts"] = aws_sdk_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    return out
