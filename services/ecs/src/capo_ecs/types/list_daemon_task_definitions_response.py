"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonTaskDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_task_definition_summaries
    import capo_ecs.types.string


class ListDaemonTaskDefinitionsResponse(TypedDict, closed=True):
    daemon_task_definitions: NotRequired[
        "capo_ecs.types.daemon_task_definition_summaries.DaemonTaskDefinitionSummaries"
    ]
    """<p>The list of daemon task definition summaries.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListDaemonTaskDefinitions</code> request. When the results of a <code>ListDaemonTaskDefinitions</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDaemonTaskDefinitionsResponse) -> dict:
    out: dict = {}
    if "daemon_task_definitions" in value:
        import capo_ecs.types.daemon_task_definition_summaries

        out["daemonTaskDefinitions"] = (
            capo_ecs.types.daemon_task_definition_summaries.serialize_aws_json_1_1(
                value["daemon_task_definitions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDaemonTaskDefinitionsResponse:
    out: ListDaemonTaskDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("daemonTaskDefinitions") is not None:
        import capo_ecs.types.daemon_task_definition_summaries

        out["daemon_task_definitions"] = (
            capo_ecs.types.daemon_task_definition_summaries.deserialize_aws_json_1_1(
                data["daemonTaskDefinitions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
