"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_summaries_list
    import capo_ecs.types.string


class ListDaemonsResponse(TypedDict, closed=True):
    daemon_summaries_list: NotRequired[
        "capo_ecs.types.daemon_summaries_list.DaemonSummariesList"
    ]
    """<p>The list of daemon summaries.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListDaemons</code> request. When the results of a <code>ListDaemons</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDaemonsResponse) -> dict:
    out: dict = {}
    if "daemon_summaries_list" in value:
        import capo_ecs.types.daemon_summaries_list

        out["daemonSummariesList"] = (
            capo_ecs.types.daemon_summaries_list.serialize_aws_json_1_1(
                value["daemon_summaries_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDaemonsResponse:
    out: ListDaemonsResponse = {}  # type: ignore[typeddict-item]
    if "daemonSummariesList" in data:
        import capo_ecs.types.daemon_summaries_list

        out["daemon_summaries_list"] = (
            capo_ecs.types.daemon_summaries_list.deserialize_aws_json_1_1(
                data["daemonSummariesList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
