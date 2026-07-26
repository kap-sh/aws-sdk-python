"""Generated from Smithy shape ``com.amazonaws.emr#ListSessionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster_id
    import capo_emr.types.max_results_number
    import capo_emr.types.session_state_list
    import capo_emr.types.string


class ListSessionsInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster to list sessions for.</p>"""
    session_states: NotRequired["capo_emr.types.session_state_list.SessionStateList"]
    """<p>An optional filter that limits the results to sessions in the specified states.</p>"""
    next_token: NotRequired["capo_emr.types.string.String"]
    """<p>The pagination token returned by a previous <code>ListSessions</code> call. Use it to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_emr.types.max_results_number.MaxResultsNumber"]
    """<p>The maximum number of sessions to return in each page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSessionsInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "session_states" in value:
        import capo_emr.types.session_state_list

        out["SessionStates"] = capo_emr.types.session_state_list.serialize_aws_json_1_1(
            value["session_states"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSessionsInput:
    out: ListSessionsInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "SessionStates" in data:
        import capo_emr.types.session_state_list

        out["session_states"] = (
            capo_emr.types.session_state_list.deserialize_aws_json_1_1(
                data["SessionStates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
