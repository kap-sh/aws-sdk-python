"""Generated from Smithy shape ``com.amazonaws.ecs#PlacementConstraint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.placement_constraint_type
    import aws_sdk_ecs.types.string


class PlacementConstraint(TypedDict):
    type: NotRequired[
        "aws_sdk_ecs.types.placement_constraint_type.PlacementConstraintType"
    ]
    """<p>The type of constraint. Use <code>distinctInstance</code> to ensure that each task in a particular group is running on a different container instance. Use <code>memberOf</code> to restrict the selection to a group of valid candidates.</p>"""
    expression: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>A cluster query language expression to apply to the constraint. The expression can have a maximum length of 2000 characters. You can't specify an expression if the constraint type is <code>distinctInstance</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html\">Cluster query language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementConstraint) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_ecs.types.placement_constraint_type

        out["type"] = (
            aws_sdk_ecs.types.placement_constraint_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementConstraint:
    out: PlacementConstraint = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_ecs.types.placement_constraint_type

        out["type"] = (
            aws_sdk_ecs.types.placement_constraint_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "expression" in data:
        out["expression"] = data["expression"]
    return out
