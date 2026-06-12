"""Generated from Smithy shape ``com.amazonaws.connect#ListTaskTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.task_template_list


class ListTaskTemplatesResponse(TypedDict):
    task_templates: NotRequired[
        "aws_sdk_connect.types.task_template_list.TaskTemplateList"
    ]
    """<p>Provides details about a list of task templates belonging to an instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p> <important> <p>This is always returned as a null in the response.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskTemplatesResponse) -> dict:
    out: dict = {}
    if "task_templates" in value:
        import aws_sdk_connect.types.task_template_list

        out["TaskTemplates"] = aws_sdk_connect.types.task_template_list.serialize_json(
            value["task_templates"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTaskTemplatesResponse:
    out: ListTaskTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "TaskTemplates" in data:
        import aws_sdk_connect.types.task_template_list

        out["task_templates"] = (
            aws_sdk_connect.types.task_template_list.deserialize_json(
                data["TaskTemplates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
