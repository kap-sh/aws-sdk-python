"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_summary

CollectionGroupSummaries: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.collection_group_summary.CollectionGroupSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupSummaries) -> list:
    import aws_sdk_opensearchserverless.types.collection_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearchserverless.types.collection_group_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CollectionGroupSummaries:
    import aws_sdk_opensearchserverless.types.collection_group_summary

    out: CollectionGroupSummaries = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.collection_group_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
