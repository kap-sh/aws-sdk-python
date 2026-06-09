"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorFiltersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_filter_set


class DescribeTrafficMirrorFiltersResult(TypedDict):
    traffic_mirror_filters: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_set.TrafficMirrorFilterSet"
    ]
    """<p>Information about one or more Traffic Mirror filters.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrafficMirrorFiltersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_mirror_filters" in value:
        import aws_sdk_ec2.types.traffic_mirror_filter_set

        aws_sdk_ec2.types.traffic_mirror_filter_set.serialize_ec2_query(
            value["traffic_mirror_filters"], pairs, f"{prefix}.TrafficMirrorFilterSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTrafficMirrorFiltersResult:
    out: DescribeTrafficMirrorFiltersResult = {}  # type: ignore[typeddict-item]
    if el.find("TrafficMirrorFilterSet") is not None:
        import aws_sdk_ec2.types.traffic_mirror_filter_set

        out["traffic_mirror_filters"] = (
            aws_sdk_ec2.types.traffic_mirror_filter_set.deserialize_ec2_query(
                el, "TrafficMirrorFilterSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
