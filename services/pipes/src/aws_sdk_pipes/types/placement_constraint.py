"""Generated from Smithy shape ``com.amazonaws.pipes#PlacementConstraint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.placement_constraint_expression
    import aws_sdk_pipes.types.placement_constraint_type


class PlacementConstraint(TypedDict):
    type: NotRequired[
        "aws_sdk_pipes.types.placement_constraint_type.PlacementConstraintType"
    ]
    """<p>The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates. </p>"""
    expression: NotRequired[
        "aws_sdk_pipes.types.placement_constraint_expression.PlacementConstraintExpression"
    ]
    """<p>A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is <code>distinctInstance</code>. To learn more, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html\">Cluster Query Language</a> in the Amazon Elastic Container Service Developer Guide. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlacementConstraint) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> PlacementConstraint:
    out: PlacementConstraint = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "expression" in data:
        out["expression"] = data["expression"]
    return out
