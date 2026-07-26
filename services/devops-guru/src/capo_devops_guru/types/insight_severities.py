"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightSeverities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_severity

InsightSeverities: TypeAlias = list[
    "capo_devops_guru.types.insight_severity.InsightSeverity"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightSeverities) -> list:
    import capo_devops_guru.types.insight_severity

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.insight_severity.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightSeverities:
    import capo_devops_guru.types.insight_severity

    out: InsightSeverities = []
    for item in data:
        out.append(capo_devops_guru.types.insight_severity.deserialize_json(item))
    return out
