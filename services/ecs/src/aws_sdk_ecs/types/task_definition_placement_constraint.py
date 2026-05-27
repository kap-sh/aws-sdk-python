"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionPlacementConstraint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.task_definition_placement_constraint_type


class TaskDefinitionPlacementConstraint(TypedDict):
    type: NotRequired[
        "aws_sdk_ecs.types.task_definition_placement_constraint_type.TaskDefinitionPlacementConstraintType"
    ]
    """<p>The type of constraint. The <code>MemberOf</code> constraint restricts selection to be from a group of valid candidates.</p>"""
    expression: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>A cluster query language expression to apply to the constraint. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html\">Cluster query language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
