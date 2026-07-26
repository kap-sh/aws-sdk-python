"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfFindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.ocsf_finding

OcsfFindingsList: TypeAlias = list["capo_securityhub.types.ocsf_finding.OcsfFinding"]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfFindingsList) -> list:
    return list(value)


def deserialize_json(data: list) -> OcsfFindingsList:
    return list(data)
