"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListFeatureGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_group_summaries
    import aws_sdk_sagemaker.types.next_token


class ListFeatureGroupsResponse(TypedDict, closed=True):
    feature_group_summaries: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_summaries.FeatureGroupSummaries"
    ]
    """<p>A summary of feature groups.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token to resume pagination of <code>ListFeatureGroups</code> results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFeatureGroupsResponse) -> dict:
    out: dict = {}
    if "feature_group_summaries" in value:
        import aws_sdk_sagemaker.types.feature_group_summaries

        out["FeatureGroupSummaries"] = (
            aws_sdk_sagemaker.types.feature_group_summaries.serialize_aws_json_1_1(
                value["feature_group_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFeatureGroupsResponse:
    out: ListFeatureGroupsResponse = {}  # type: ignore[typeddict-item]
    if "FeatureGroupSummaries" in data:
        import aws_sdk_sagemaker.types.feature_group_summaries

        out["feature_group_summaries"] = (
            aws_sdk_sagemaker.types.feature_group_summaries.deserialize_aws_json_1_1(
                data["FeatureGroupSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
