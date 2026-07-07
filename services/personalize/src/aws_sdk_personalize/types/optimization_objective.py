"""Generated from Smithy shape ``com.amazonaws.personalize#OptimizationObjective``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.item_attribute
    import aws_sdk_personalize.types.objective_sensitivity


class OptimizationObjective(TypedDict, closed=True):
    item_attribute: NotRequired[
        "aws_sdk_personalize.types.item_attribute.ItemAttribute"
    ]
    """<p>The numerical metadata column in an Items dataset related to the optimization objective. For example, VIDEO_LENGTH (to maximize streaming minutes), or PRICE (to maximize revenue).</p>"""
    objective_sensitivity: NotRequired[
        "aws_sdk_personalize.types.objective_sensitivity.ObjectiveSensitivity"
    ]
    """<p>Specifies how Amazon Personalize balances the importance of your optimization objective versus relevance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationObjective) -> dict:
    out: dict = {}
    if "item_attribute" in value:
        out["itemAttribute"] = value["item_attribute"]
    if "objective_sensitivity" in value:
        import aws_sdk_personalize.types.objective_sensitivity

        out["objectiveSensitivity"] = (
            aws_sdk_personalize.types.objective_sensitivity.serialize_aws_json_1_1(
                value["objective_sensitivity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationObjective:
    out: OptimizationObjective = {}  # type: ignore[typeddict-item]
    if "itemAttribute" in data:
        out["item_attribute"] = data["itemAttribute"]
    if "objectiveSensitivity" in data:
        import aws_sdk_personalize.types.objective_sensitivity

        out["objective_sensitivity"] = (
            aws_sdk_personalize.types.objective_sensitivity.deserialize_aws_json_1_1(
                data["objectiveSensitivity"]
            )
        )
    return out
