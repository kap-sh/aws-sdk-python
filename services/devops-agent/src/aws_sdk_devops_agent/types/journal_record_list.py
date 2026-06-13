"""Generated from Smithy shape ``com.amazonaws.devopsagent#JournalRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.journal_record

JournalRecordList: TypeAlias = list[
    "aws_sdk_devops_agent.types.journal_record.JournalRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: JournalRecordList) -> list:
    import aws_sdk_devops_agent.types.journal_record

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.journal_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> JournalRecordList:
    import aws_sdk_devops_agent.types.journal_record

    out: JournalRecordList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.journal_record.deserialize_json(item))
    return out
