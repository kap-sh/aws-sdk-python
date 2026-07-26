"""Generated from Smithy shape ``com.amazonaws.ssmincidents#FindingIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.finding_id

FindingIdList: TypeAlias = list["capo_ssm_incidents.types.finding_id.FindingId"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> FindingIdList:
    return list(data)
