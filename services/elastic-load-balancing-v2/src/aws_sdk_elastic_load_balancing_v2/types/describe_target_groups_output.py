"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTargetGroupsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.marker
    import aws_sdk_elastic_load_balancing_v2.types.target_groups


class DescribeTargetGroupsOutput(TypedDict):
    target_groups: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_groups.TargetGroups"
    ]
    """<p>Information about the target groups.</p>"""
    next_marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTargetGroupsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_groups" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_groups

        aws_sdk_elastic_load_balancing_v2.types.target_groups.serialize_query(
            value["target_groups"], pairs, f"{prefix}.TargetGroups"
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeTargetGroupsOutput:
    out: DescribeTargetGroupsOutput = {}  # type: ignore[typeddict-item]
    child_target_groups = el.find("TargetGroups")
    if child_target_groups is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_groups

        out["target_groups"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_groups.deserialize_query(
                child_target_groups
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
