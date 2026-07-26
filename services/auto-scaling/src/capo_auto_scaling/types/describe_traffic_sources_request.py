"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeTrafficSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.xml_string
    import capo_auto_scaling.types.xml_string_max_len255


class DescribeTrafficSourcesRequest(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    traffic_source_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The traffic source type that you want to describe.</p> <p>The following lists the valid values:</p> <ul> <li> <p> <code>elb</code> if the traffic source is a Classic Load Balancer.</p> </li> <li> <p> <code>elbv2</code> if the traffic source is a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer.</p> </li> <li> <p> <code>vpc-lattice</code> if the traffic source is VPC Lattice.</p> </li> </ul>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["capo_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The maximum value is <code>50</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrafficSourcesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "traffic_source_type" in value:
        pairs.append((f"{prefix}.TrafficSourceType", str(value["traffic_source_type"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeTrafficSourcesRequest:
    out: DescribeTrafficSourcesRequest = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_traffic_source_type = el.find("TrafficSourceType")
    if child_traffic_source_type is not None:
        out["traffic_source_type"] = str(child_traffic_source_type.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
