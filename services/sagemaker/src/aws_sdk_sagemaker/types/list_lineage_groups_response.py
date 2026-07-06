"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListLineageGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.lineage_group_summaries
    import aws_sdk_sagemaker.types.next_token


class ListLineageGroupsResponse(TypedDict, closed=True):
    lineage_group_summaries: NotRequired[
        "aws_sdk_sagemaker.types.lineage_group_summaries.LineageGroupSummaries"
    ]
    """<p>A list of lineage groups and their properties.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of algorithms, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLineageGroupsResponse) -> dict:
    out: dict = {}
    if "lineage_group_summaries" in value:
        import aws_sdk_sagemaker.types.lineage_group_summaries

        out["LineageGroupSummaries"] = (
            aws_sdk_sagemaker.types.lineage_group_summaries.serialize_aws_json_1_1(
                value["lineage_group_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLineageGroupsResponse:
    out: ListLineageGroupsResponse = {}  # type: ignore[typeddict-item]
    if "LineageGroupSummaries" in data:
        import aws_sdk_sagemaker.types.lineage_group_summaries

        out["lineage_group_summaries"] = (
            aws_sdk_sagemaker.types.lineage_group_summaries.deserialize_aws_json_1_1(
                data["LineageGroupSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
