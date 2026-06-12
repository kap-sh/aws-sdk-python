"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServicePlacementConstraintsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsServicePlacementConstraintsDetails(TypedDict):
    expression: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is <code>distinctInstance</code>.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of constraint. Use <code>distinctInstance</code> to run each task in a particular group on a different container instance. Use <code>memberOf</code> to restrict the selection to a group of valid candidates.</p> <p>Valid values: <code>distinctInstance</code> | <code>memberOf</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServicePlacementConstraintsDetails) -> dict:
    out: dict = {}
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsEcsServicePlacementConstraintsDetails:
    out: AwsEcsServicePlacementConstraintsDetails = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
