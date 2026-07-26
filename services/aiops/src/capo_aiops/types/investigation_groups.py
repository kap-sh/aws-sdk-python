"""Generated from Smithy shape ``com.amazonaws.aiops#InvestigationGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_aiops.types.list_investigation_groups_model

InvestigationGroups: TypeAlias = list[
    "capo_aiops.types.list_investigation_groups_model.ListInvestigationGroupsModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationGroups) -> list:
    import capo_aiops.types.list_investigation_groups_model

    out: list = []
    for item in value:
        out.append(
            capo_aiops.types.list_investigation_groups_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InvestigationGroups:
    import capo_aiops.types.list_investigation_groups_model

    out: InvestigationGroups = []
    for item in data:
        out.append(
            capo_aiops.types.list_investigation_groups_model.deserialize_json(item)
        )
    return out
