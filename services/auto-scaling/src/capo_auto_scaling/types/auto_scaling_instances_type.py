"""Generated from Smithy shape ``com.amazonaws.autoscaling#AutoScalingInstancesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_instances
    import capo_auto_scaling.types.xml_string


class AutoScalingInstancesType(TypedDict, closed=True):
    auto_scaling_instances: NotRequired[
        "capo_auto_scaling.types.auto_scaling_instances.AutoScalingInstances"
    ]
    """<p>The instances.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoScalingInstancesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_instances" in value:
        import capo_auto_scaling.types.auto_scaling_instances

        capo_auto_scaling.types.auto_scaling_instances.serialize_query(
            value["auto_scaling_instances"], pairs, f"{prefix}.AutoScalingInstances"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> AutoScalingInstancesType:
    out: AutoScalingInstancesType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_instances = el.find("AutoScalingInstances")
    if child_auto_scaling_instances is not None:
        import capo_auto_scaling.types.auto_scaling_instances

        out["auto_scaling_instances"] = (
            capo_auto_scaling.types.auto_scaling_instances.deserialize_query(
                child_auto_scaling_instances
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
