"""Generated from Smithy shape ``com.amazonaws.autoscaling#DetachTrafficSourcesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.traffic_sources
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class DetachTrafficSourcesType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    traffic_sources: NotRequired[
        "aws_sdk_auto_scaling.types.traffic_sources.TrafficSources"
    ]
    """<p>The unique identifiers of one or more traffic sources. You can specify up to 10 traffic sources.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetachTrafficSourcesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "traffic_sources" in value:
        import aws_sdk_auto_scaling.types.traffic_sources

        aws_sdk_auto_scaling.types.traffic_sources.serialize_query(
            value["traffic_sources"], pairs, f"{prefix}.TrafficSources"
        )


def deserialize_query(el: Element) -> DetachTrafficSourcesType:
    out: DetachTrafficSourcesType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_traffic_sources = el.find("TrafficSources")
    if child_traffic_sources is not None:
        import aws_sdk_auto_scaling.types.traffic_sources

        out["traffic_sources"] = (
            aws_sdk_auto_scaling.types.traffic_sources.deserialize_query(
                child_traffic_sources
            )
        )
    return out
