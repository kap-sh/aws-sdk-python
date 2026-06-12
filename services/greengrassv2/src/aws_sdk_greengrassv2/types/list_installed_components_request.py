"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListInstalledComponentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.core_device_thing_name
    import aws_sdk_greengrassv2.types.default_max_results
    import aws_sdk_greengrassv2.types.installed_component_topology_filter
    import aws_sdk_greengrassv2.types.next_token_string


class ListInstalledComponentsRequest(TypedDict):
    core_device_thing_name: (
        "aws_sdk_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    )
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""
    max_results: NotRequired[
        "aws_sdk_greengrassv2.types.default_max_results.DefaultMaxResults"
    ]
    """<p>The maximum number of results to be returned per paginated request.</p>"""
    next_token: NotRequired[
        "aws_sdk_greengrassv2.types.next_token_string.NextTokenString"
    ]
    """<p>The token to be used for the next set of paginated results.</p>"""
    topology_filter: NotRequired[
        "aws_sdk_greengrassv2.types.installed_component_topology_filter.InstalledComponentTopologyFilter"
    ]
    """<p>The filter for the list of components. Choose from the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all components installed on the core device.</p> </li> <li> <p> <code>ROOT</code> – The list includes only <i>root</i> components, which are components that you specify in a deployment. When you choose this option, the list doesn't include components that the core device installs as dependencies of other components.</p> </li> </ul> <p>Default: <code>ROOT</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstalledComponentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInstalledComponentsRequest:
    out: ListInstalledComponentsRequest = {}  # type: ignore[typeddict-item]
    return out
