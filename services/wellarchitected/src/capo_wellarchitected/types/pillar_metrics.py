"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.pillar_metric

PillarMetrics: TypeAlias = list["capo_wellarchitected.types.pillar_metric.PillarMetric"]


# --- restJson1 ser/de ---
def serialize_json(value: PillarMetrics) -> list:
    import capo_wellarchitected.types.pillar_metric

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.pillar_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> PillarMetrics:
    import capo_wellarchitected.types.pillar_metric

    out: PillarMetrics = []
    for item in data:
        out.append(capo_wellarchitected.types.pillar_metric.deserialize_json(item))
    return out
