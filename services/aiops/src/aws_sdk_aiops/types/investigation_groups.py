"""Generated from Smithy shape ``com.amazonaws.aiops#InvestigationGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_aiops.types.list_investigation_groups_model

InvestigationGroups: TypeAlias = list[
    "aws_sdk_aiops.types.list_investigation_groups_model.ListInvestigationGroupsModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationGroups) -> list:
    import aws_sdk_aiops.types.list_investigation_groups_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_aiops.types.list_investigation_groups_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InvestigationGroups:
    import aws_sdk_aiops.types.list_investigation_groups_model

    out: InvestigationGroups = []
    for item in data:
        out.append(
            aws_sdk_aiops.types.list_investigation_groups_model.deserialize_json(item)
        )
    return out
