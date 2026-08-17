"""Generated from Smithy shape ``com.amazonaws.ecr#ListPullTimeUpdateExclusionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.next_token
    import capo_ecr.types.pull_time_update_exclusion_list


class ListPullTimeUpdateExclusionsResponse(TypedDict, closed=True):
    pull_time_update_exclusions: NotRequired[
        "capo_ecr.types.pull_time_update_exclusion_list.PullTimeUpdateExclusionList"
    ]
    """<p>The list of IAM principal ARNs that are excluded from having their image pull times recorded.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListPullTimeUpdateExclusions</code> request. When the results of a <code>ListPullTimeUpdateExclusions</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPullTimeUpdateExclusionsResponse) -> dict:
    out: dict = {}
    if "pull_time_update_exclusions" in value:
        import capo_ecr.types.pull_time_update_exclusion_list

        out["pullTimeUpdateExclusions"] = (
            capo_ecr.types.pull_time_update_exclusion_list.serialize_aws_json_1_1(
                value["pull_time_update_exclusions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPullTimeUpdateExclusionsResponse:
    out: ListPullTimeUpdateExclusionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("pullTimeUpdateExclusions") is not None:
        import capo_ecr.types.pull_time_update_exclusion_list

        out["pull_time_update_exclusions"] = (
            capo_ecr.types.pull_time_update_exclusion_list.deserialize_aws_json_1_1(
                data["pullTimeUpdateExclusions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
