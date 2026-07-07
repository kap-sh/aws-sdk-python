"""Generated from Smithy shape ``com.amazonaws.autoscaling#AutoScalingGroupsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.auto_scaling_groups
    import aws_sdk_auto_scaling.types.xml_string


class AutoScalingGroupsType(TypedDict, closed=True):
    auto_scaling_groups: NotRequired[
        "aws_sdk_auto_scaling.types.auto_scaling_groups.AutoScalingGroups"
    ]
    """<p>The groups.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoScalingGroupsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_groups" in value:
        import aws_sdk_auto_scaling.types.auto_scaling_groups

        aws_sdk_auto_scaling.types.auto_scaling_groups.serialize_query(
            value["auto_scaling_groups"], pairs, f"{prefix}.AutoScalingGroups"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> AutoScalingGroupsType:
    out: AutoScalingGroupsType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_groups = el.find("AutoScalingGroups")
    if child_auto_scaling_groups is not None:
        import aws_sdk_auto_scaling.types.auto_scaling_groups

        out["auto_scaling_groups"] = (
            aws_sdk_auto_scaling.types.auto_scaling_groups.deserialize_query(
                child_auto_scaling_groups
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
