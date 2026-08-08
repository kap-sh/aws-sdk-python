"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacModificationTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_mac_modification_tasks_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.mac_modification_task_id_list
    import capo_ec2.types.string


class DescribeMacModificationTasksRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>Specifies one or more filters for the request:</p> <ul> <li> <p> <code>instance-id</code> - The ID of the instance for which the task was created.</p> </li> <li> <p> <code>task-state</code> - The state of the task (<code>successful</code> | <code>failed</code> | <code>in-progress</code> | <code>pending</code>).</p> </li> <li> <p> <code>mac-system-integrity-protection-configuration.sip-status</code> - The overall SIP state requested in the task (<code>enabled</code> | <code>disabled</code>).</p> </li> <li> <p> <code>start-time</code> - The date and time the task was created.</p> </li> <li> <p> <code>task-type</code> - The type of task (<code>sip-modification</code> | <code>volume-ownership-delegation</code>).</p> </li> </ul>"""
    mac_modification_task_ids: NotRequired[
        "capo_ec2.types.mac_modification_task_id_list.MacModificationTaskIdList"
    ]
    """<p>The ID of task.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_mac_modification_tasks_max_results.DescribeMacModificationTasksMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeMacModificationTasksRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "mac_modification_task_ids" in value:
        import capo_ec2.types.mac_modification_task_id_list

        capo_ec2.types.mac_modification_task_id_list.serialize_ec2_query(
            value["mac_modification_task_ids"],
            pairs,
            f"{key_prefix}MacModificationTaskId",
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeMacModificationTasksRequest:
    out: DescribeMacModificationTasksRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    if el.find("MacModificationTaskId") is not None:
        import capo_ec2.types.mac_modification_task_id_list

        out["mac_modification_task_ids"] = (
            capo_ec2.types.mac_modification_task_id_list.deserialize_ec2_query(
                el, "MacModificationTaskId"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
