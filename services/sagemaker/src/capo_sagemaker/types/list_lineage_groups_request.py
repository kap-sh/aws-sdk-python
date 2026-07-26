"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListLineageGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_lineage_groups_by
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListLineageGroupsRequest(TypedDict, closed=True):
    created_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp to filter against lineage groups created after a certain point in time.</p>"""
    created_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp to filter against lineage groups created before a certain point in time.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.sort_lineage_groups_by.SortLineageGroupsBy"
    ]
    """<p>The parameter by which to sort the results. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for the results. The default is <code>Ascending</code>.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of algorithms, use it in the subsequent request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of endpoints to return in the response. This value defaults to 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLineageGroupsRequest) -> dict:
    out: dict = {}
    if "created_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedAfter"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedBefore"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "sort_by" in value:
        import capo_sagemaker.types.sort_lineage_groups_by

        out["SortBy"] = (
            capo_sagemaker.types.sort_lineage_groups_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLineageGroupsRequest:
    out: ListLineageGroupsRequest = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import capo_sagemaker.types.timestamp

        out["created_after"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if "CreatedBefore" in data:
        import capo_sagemaker.types.timestamp

        out["created_before"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if "SortBy" in data:
        import capo_sagemaker.types.sort_lineage_groups_by

        out["sort_by"] = (
            capo_sagemaker.types.sort_lineage_groups_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
