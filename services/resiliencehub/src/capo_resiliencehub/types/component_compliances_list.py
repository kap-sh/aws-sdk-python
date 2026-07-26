"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ComponentCompliancesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_component_compliance

ComponentCompliancesList: TypeAlias = list[
    "capo_resiliencehub.types.app_component_compliance.AppComponentCompliance"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentCompliancesList) -> list:
    import capo_resiliencehub.types.app_component_compliance

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehub.types.app_component_compliance.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComponentCompliancesList:
    import capo_resiliencehub.types.app_component_compliance

    out: ComponentCompliancesList = []
    for item in data:
        out.append(
            capo_resiliencehub.types.app_component_compliance.deserialize_json(item)
        )
    return out
