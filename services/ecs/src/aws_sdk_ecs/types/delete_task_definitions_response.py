"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteTaskDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.task_definition_list


class DeleteTaskDefinitionsResponse(TypedDict):
    task_definitions: NotRequired[
        "aws_sdk_ecs.types.task_definition_list.TaskDefinitionList"
    ]
    """<p>The list of deleted task definitions.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
