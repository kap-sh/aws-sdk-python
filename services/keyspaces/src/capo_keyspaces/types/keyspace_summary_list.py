"""Generated from Smithy shape ``com.amazonaws.keyspaces#KeyspaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.keyspace_summary

KeyspaceSummaryList: TypeAlias = list[
    "capo_keyspaces.types.keyspace_summary.KeyspaceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspaceSummaryList) -> list:
    import capo_keyspaces.types.keyspace_summary

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.keyspace_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> KeyspaceSummaryList:
    import capo_keyspaces.types.keyspace_summary

    out: KeyspaceSummaryList = []
    for item in data:
        out.append(capo_keyspaces.types.keyspace_summary.deserialize_aws_json_1_0(item))
    return out
