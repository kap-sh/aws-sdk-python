"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_status

InsightStatuses: TypeAlias = list["capo_devops_guru.types.insight_status.InsightStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightStatuses) -> list:
    import capo_devops_guru.types.insight_status

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.insight_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightStatuses:
    import capo_devops_guru.types.insight_status

    out: InsightStatuses = []
    for item in data:
        out.append(capo_devops_guru.types.insight_status.deserialize_json(item))
    return out
