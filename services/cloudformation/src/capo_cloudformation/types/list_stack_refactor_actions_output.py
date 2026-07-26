"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackRefactorActionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stack_refactor_actions


class ListStackRefactorActionsOutput(TypedDict, closed=True):
    stack_refactor_actions: NotRequired[
        "capo_cloudformation.types.stack_refactor_actions.StackRefactorActions"
    ]
    """<p>The stack refactor actions.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackRefactorActionsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_refactor_actions" in value:
        import capo_cloudformation.types.stack_refactor_actions

        capo_cloudformation.types.stack_refactor_actions.serialize_query(
            value["stack_refactor_actions"], pairs, f"{prefix}.StackRefactorActions"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackRefactorActionsOutput:
    out: ListStackRefactorActionsOutput = {}  # type: ignore[typeddict-item]
    child_stack_refactor_actions = el.find("StackRefactorActions")
    if child_stack_refactor_actions is not None:
        import capo_cloudformation.types.stack_refactor_actions

        out["stack_refactor_actions"] = (
            capo_cloudformation.types.stack_refactor_actions.deserialize_query(
                child_stack_refactor_actions
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
