"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#RecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.record

RecordList: TypeAlias = list["capo_keyspacesstreams.types.record.Record"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecordList) -> list:
    import capo_keyspacesstreams.types.record

    out: list = []
    for item in value:
        out.append(capo_keyspacesstreams.types.record.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RecordList:
    import capo_keyspacesstreams.types.record

    out: RecordList = []
    for item in data:
        out.append(capo_keyspacesstreams.types.record.deserialize_aws_json_1_0(item))
    return out
