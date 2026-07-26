"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_summary

CollectionSummaries: TypeAlias = list[
    "capo_opensearchserverless.types.collection_summary.CollectionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionSummaries) -> list:
    import capo_opensearchserverless.types.collection_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.collection_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CollectionSummaries:
    import capo_opensearchserverless.types.collection_summary

    out: CollectionSummaries = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.collection_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
