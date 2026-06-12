"""Generated from Smithy shape ``com.amazonaws.snowball#ClusterListEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.cluster_list_entry

ClusterListEntryList: TypeAlias = list[
    "aws_sdk_snowball.types.cluster_list_entry.ClusterListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterListEntryList) -> list:
    import aws_sdk_snowball.types.cluster_list_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_snowball.types.cluster_list_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterListEntryList:
    import aws_sdk_snowball.types.cluster_list_entry

    out: ClusterListEntryList = []
    for item in data:
        out.append(
            aws_sdk_snowball.types.cluster_list_entry.deserialize_aws_json_1_1(item)
        )
    return out
