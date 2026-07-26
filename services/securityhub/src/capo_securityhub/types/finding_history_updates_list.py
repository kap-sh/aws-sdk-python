"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryUpdatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.finding_history_update

FindingHistoryUpdatesList: TypeAlias = list[
    "capo_securityhub.types.finding_history_update.FindingHistoryUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryUpdatesList) -> list:
    import capo_securityhub.types.finding_history_update

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.finding_history_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingHistoryUpdatesList:
    import capo_securityhub.types.finding_history_update

    out: FindingHistoryUpdatesList = []
    for item in data:
        out.append(capo_securityhub.types.finding_history_update.deserialize_json(item))
    return out
