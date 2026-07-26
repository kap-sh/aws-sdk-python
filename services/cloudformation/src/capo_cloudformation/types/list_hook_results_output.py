"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListHookResultsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.hook_result_id
    import capo_cloudformation.types.hook_result_summaries
    import capo_cloudformation.types.list_hook_results_target_type
    import capo_cloudformation.types.next_token


class ListHookResultsOutput(TypedDict, closed=True):
    target_type: NotRequired[
        "capo_cloudformation.types.list_hook_results_target_type.ListHookResultsTargetType"
    ]
    """<p>The target type.</p>"""
    target_id: NotRequired["capo_cloudformation.types.hook_result_id.HookResultId"]
    """<p>The unique identifier of the Hook invocation target.</p>"""
    hook_results: NotRequired[
        "capo_cloudformation.types.hook_result_summaries.HookResultSummaries"
    ]
    """<p>A list of <code>HookResultSummary</code> structures that provides the status and Hook status reason for each Hook invocation for the specified target.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>Pagination token, <code>null</code> or empty if no more results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListHookResultsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_type" in value:
        import capo_cloudformation.types.list_hook_results_target_type

        capo_cloudformation.types.list_hook_results_target_type.serialize_query(
            value["target_type"], pairs, f"{prefix}.TargetType"
        )
    if "target_id" in value:
        pairs.append((f"{prefix}.TargetId", str(value["target_id"])))
    if "hook_results" in value:
        import capo_cloudformation.types.hook_result_summaries

        capo_cloudformation.types.hook_result_summaries.serialize_query(
            value["hook_results"], pairs, f"{prefix}.HookResults"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListHookResultsOutput:
    out: ListHookResultsOutput = {}  # type: ignore[typeddict-item]
    child_target_type = el.find("TargetType")
    if child_target_type is not None:
        import capo_cloudformation.types.list_hook_results_target_type

        out["target_type"] = (
            capo_cloudformation.types.list_hook_results_target_type.deserialize_query(
                child_target_type
            )
        )
    child_target_id = el.find("TargetId")
    if child_target_id is not None:
        out["target_id"] = str(child_target_id.text or "")
    child_hook_results = el.find("HookResults")
    if child_hook_results is not None:
        import capo_cloudformation.types.hook_result_summaries

        out["hook_results"] = (
            capo_cloudformation.types.hook_result_summaries.deserialize_query(
                child_hook_results
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
