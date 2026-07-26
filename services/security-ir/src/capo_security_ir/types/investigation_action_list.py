"""Generated from Smithy shape ``com.amazonaws.securityir#InvestigationActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.investigation_action

InvestigationActionList: TypeAlias = list[
    "capo_security_ir.types.investigation_action.InvestigationAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationActionList) -> list:
    import capo_security_ir.types.investigation_action

    out: list = []
    for item in value:
        out.append(capo_security_ir.types.investigation_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> InvestigationActionList:
    import capo_security_ir.types.investigation_action

    out: InvestigationActionList = []
    for item in data:
        out.append(capo_security_ir.types.investigation_action.deserialize_json(item))
    return out
