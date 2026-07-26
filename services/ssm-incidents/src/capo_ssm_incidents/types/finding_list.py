"""Generated from Smithy shape ``com.amazonaws.ssmincidents#FindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.finding

FindingList: TypeAlias = list["capo_ssm_incidents.types.finding.Finding"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingList) -> list:
    import capo_ssm_incidents.types.finding

    out: list = []
    for item in value:
        out.append(capo_ssm_incidents.types.finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingList:
    import capo_ssm_incidents.types.finding

    out: FindingList = []
    for item in data:
        out.append(capo_ssm_incidents.types.finding.deserialize_json(item))
    return out
