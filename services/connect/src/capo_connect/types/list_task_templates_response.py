"""Generated from Smithy shape ``com.amazonaws.connect#ListTaskTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.task_template_list


class ListTaskTemplatesResponse(TypedDict, closed=True):
    task_templates: NotRequired[
        "capo_connect.types.task_template_list.TaskTemplateList"
    ]
    """<p>Provides details about a list of task templates belonging to an instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p> <important> <p>This is always returned as a null in the response.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskTemplatesResponse) -> dict:
    out: dict = {}
    if "task_templates" in value:
        import capo_connect.types.task_template_list

        out["TaskTemplates"] = capo_connect.types.task_template_list.serialize_json(
            value["task_templates"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTaskTemplatesResponse:
    out: ListTaskTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "TaskTemplates" in data:
        import capo_connect.types.task_template_list

        out["task_templates"] = capo_connect.types.task_template_list.deserialize_json(
            data["TaskTemplates"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
