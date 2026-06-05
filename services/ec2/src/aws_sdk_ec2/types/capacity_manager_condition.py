"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerCondition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dimension_condition


class CapacityManagerCondition(TypedDict):
    dimension_condition: NotRequired[
        "aws_sdk_ec2.types.dimension_condition.DimensionCondition"
    ]
    """<p> The dimension-based condition that specifies how to filter the data based on dimension values. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerCondition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dimension_condition" in value:
        import aws_sdk_ec2.types.dimension_condition

        aws_sdk_ec2.types.dimension_condition.serialize_ec2_query(
            value["dimension_condition"], pairs, f"{prefix}.DimensionCondition"
        )


def deserialize_ec2_query(el: Element) -> CapacityManagerCondition:
    out: CapacityManagerCondition = {}  # type: ignore[typeddict-item]
    child_dimension_condition = el.find("DimensionCondition")
    if child_dimension_condition is not None:
        import aws_sdk_ec2.types.dimension_condition

        out["dimension_condition"] = (
            aws_sdk_ec2.types.dimension_condition.deserialize_ec2_query(
                child_dimension_condition
            )
        )
    return out
