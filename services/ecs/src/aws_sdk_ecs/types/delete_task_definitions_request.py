"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteTaskDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class DeleteTaskDefinitionsRequest(TypedDict):
    task_definitions: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to delete. You must specify a <code>revision</code>.</p> <p>You can specify up to 10 task definitions as a comma separated list.</p>"""
