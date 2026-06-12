"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.finding_history_record

FindingHistoryRecordList: TypeAlias = list[
    "aws_sdk_securityhub.types.finding_history_record.FindingHistoryRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryRecordList) -> list:
    import aws_sdk_securityhub.types.finding_history_record

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.finding_history_record.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingHistoryRecordList:
    import aws_sdk_securityhub.types.finding_history_record

    out: FindingHistoryRecordList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.finding_history_record.deserialize_json(item)
        )
    return out
