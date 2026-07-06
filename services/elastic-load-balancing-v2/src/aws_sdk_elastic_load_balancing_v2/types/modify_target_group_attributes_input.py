"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyTargetGroupAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.target_group_arn
    import aws_sdk_elastic_load_balancing_v2.types.target_group_attributes


class ModifyTargetGroupAttributesInput(TypedDict, closed=True):
    target_group_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    attributes: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_attributes.TargetGroupAttributes"
    ]
    """<p>The target group attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyTargetGroupAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_group_arn" in value:
        pairs.append((f"{prefix}.TargetGroupArn", str(value["target_group_arn"])))
    if "attributes" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_attributes

        aws_sdk_elastic_load_balancing_v2.types.target_group_attributes.serialize_query(
            value["attributes"], pairs, f"{prefix}.Attributes"
        )


def deserialize_query(el: Element) -> ModifyTargetGroupAttributesInput:
    out: ModifyTargetGroupAttributesInput = {}  # type: ignore[typeddict-item]
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_attributes

        out["attributes"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_group_attributes.deserialize_query(
                child_attributes
            )
        )
    return out
