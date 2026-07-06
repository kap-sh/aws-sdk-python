"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionPlacementConstraintsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionPlacementConstraintsDetails(TypedDict, closed=True):
    expression: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A cluster query language expression to apply to the constraint.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of constraint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionPlacementConstraintsDetails) -> dict:
    out: dict = {}
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsEcsTaskDefinitionPlacementConstraintsDetails:
    out: AwsEcsTaskDefinitionPlacementConstraintsDetails = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
