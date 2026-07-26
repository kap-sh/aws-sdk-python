"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacModificationTasksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.mac_modification_task_list
    import capo_ec2.types.string


class DescribeMacModificationTasksResult(TypedDict, closed=True):
    mac_modification_tasks: NotRequired[
        "capo_ec2.types.mac_modification_task_list.MacModificationTaskList"
    ]
    """<p>Information about the tasks.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeMacModificationTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "mac_modification_tasks" in value:
        import capo_ec2.types.mac_modification_task_list

        capo_ec2.types.mac_modification_task_list.serialize_ec2_query(
            value["mac_modification_tasks"], pairs, f"{prefix}.MacModificationTaskSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeMacModificationTasksResult:
    out: DescribeMacModificationTasksResult = {}  # type: ignore[typeddict-item]
    if el.find("MacModificationTaskSet") is not None:
        import capo_ec2.types.mac_modification_task_list

        out["mac_modification_tasks"] = (
            capo_ec2.types.mac_modification_task_list.deserialize_ec2_query(
                el, "MacModificationTaskSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
