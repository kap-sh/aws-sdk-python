"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterNetworkServicesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.traffic_mirror_filter_id
    import aws_sdk_ec2.types.traffic_mirror_network_service_list


class ModifyTrafficMirrorFilterNetworkServicesRequest(TypedDict):
    traffic_mirror_filter_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    add_network_services: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_network_service_list.TrafficMirrorNetworkServiceList"
    ]
    """<p>The network service, for example Amazon DNS, that you want to mirror.</p>"""
    remove_network_services: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_network_service_list.TrafficMirrorNetworkServiceList"
    ]
    """<p>The network service, for example Amazon DNS, that you no longer want to mirror.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
