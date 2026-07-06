"""Generated from Smithy shape ``com.amazonaws.fms#ListResourceSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.pagination_token
    import aws_sdk_fms.types.resource_set_summary_list


class ListResourceSetsResponse(TypedDict, closed=True):
    resource_sets: NotRequired[
        "aws_sdk_fms.types.resource_set_summary_list.ResourceSetSummaryList"
    ]
    """<p>An array of <code>ResourceSetSummary</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_fms.types.pagination_token.PaginationToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceSetsResponse) -> dict:
    out: dict = {}
    if "resource_sets" in value:
        import aws_sdk_fms.types.resource_set_summary_list

        out["ResourceSets"] = (
            aws_sdk_fms.types.resource_set_summary_list.serialize_aws_json_1_1(
                value["resource_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceSetsResponse:
    out: ListResourceSetsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceSets" in data:
        import aws_sdk_fms.types.resource_set_summary_list

        out["resource_sets"] = (
            aws_sdk_fms.types.resource_set_summary_list.deserialize_aws_json_1_1(
                data["ResourceSets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
