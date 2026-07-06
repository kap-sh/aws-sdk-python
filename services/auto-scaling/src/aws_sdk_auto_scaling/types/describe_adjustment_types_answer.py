"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeAdjustmentTypesAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.adjustment_types


class DescribeAdjustmentTypesAnswer(TypedDict, closed=True):
    adjustment_types: NotRequired[
        "aws_sdk_auto_scaling.types.adjustment_types.AdjustmentTypes"
    ]
    """<p>The policy adjustment types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAdjustmentTypesAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "adjustment_types" in value:
        import aws_sdk_auto_scaling.types.adjustment_types

        aws_sdk_auto_scaling.types.adjustment_types.serialize_query(
            value["adjustment_types"], pairs, f"{prefix}.AdjustmentTypes"
        )


def deserialize_query(el: Element) -> DescribeAdjustmentTypesAnswer:
    out: DescribeAdjustmentTypesAnswer = {}  # type: ignore[typeddict-item]
    child_adjustment_types = el.find("AdjustmentTypes")
    if child_adjustment_types is not None:
        import aws_sdk_auto_scaling.types.adjustment_types

        out["adjustment_types"] = (
            aws_sdk_auto_scaling.types.adjustment_types.deserialize_query(
                child_adjustment_types
            )
        )
    return out
