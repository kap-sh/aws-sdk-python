"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ComplianceDriftList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.compliance_drift

ComplianceDriftList: TypeAlias = list[
    "capo_resiliencehub.types.compliance_drift.ComplianceDrift"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComplianceDriftList) -> list:
    import capo_resiliencehub.types.compliance_drift

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.compliance_drift.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComplianceDriftList:
    import capo_resiliencehub.types.compliance_drift

    out: ComplianceDriftList = []
    for item in data:
        out.append(capo_resiliencehub.types.compliance_drift.deserialize_json(item))
    return out
