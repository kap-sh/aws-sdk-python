"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.finding_history_record

FindingHistoryRecordList: TypeAlias = list[
    "capo_securityhub.types.finding_history_record.FindingHistoryRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryRecordList) -> list:
    import capo_securityhub.types.finding_history_record

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.finding_history_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingHistoryRecordList:
    import capo_securityhub.types.finding_history_record

    out: FindingHistoryRecordList = []
    for item in data:
        out.append(capo_securityhub.types.finding_history_record.deserialize_json(item))
    return out
