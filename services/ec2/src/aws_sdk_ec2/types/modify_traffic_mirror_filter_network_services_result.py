"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterNetworkServicesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter


class ModifyTrafficMirrorFilterNetworkServicesResult(TypedDict):
    traffic_mirror_filter: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter.TrafficMirrorFilter"
    ]
    """<p>The Traffic Mirror filter that the network service is associated with.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTrafficMirrorFilterNetworkServicesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "traffic_mirror_filter" in value:
        import aws_sdk_ec2.types.traffic_mirror_filter

        aws_sdk_ec2.types.traffic_mirror_filter.serialize_ec2_query(
            value["traffic_mirror_filter"], pairs, f"{prefix}.TrafficMirrorFilter"
        )


def deserialize_ec2_query(
    el: Element,
) -> ModifyTrafficMirrorFilterNetworkServicesResult:
    out: ModifyTrafficMirrorFilterNetworkServicesResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter = el.find("TrafficMirrorFilter")
    if child_traffic_mirror_filter is not None:
        import aws_sdk_ec2.types.traffic_mirror_filter

        out["traffic_mirror_filter"] = (
            aws_sdk_ec2.types.traffic_mirror_filter.deserialize_ec2_query(
                child_traffic_mirror_filter
            )
        )
    return out
