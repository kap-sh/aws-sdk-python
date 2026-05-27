"""Generated from Smithy shape ``com.amazonaws.ecs#ProxyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.proxy_configuration_properties
    import aws_sdk_ecs.types.proxy_configuration_type
    import aws_sdk_ecs.types.string


class ProxyConfiguration(TypedDict):
    type: NotRequired[
        "aws_sdk_ecs.types.proxy_configuration_type.ProxyConfigurationType"
    ]
    """<p>The proxy type. The only supported value is <code>APPMESH</code>.</p>"""
    container_name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the container that will serve as the App Mesh proxy.</p>"""
    properties: NotRequired[
        "aws_sdk_ecs.types.proxy_configuration_properties.ProxyConfigurationProperties"
    ]
    """<p>The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.</p> <ul> <li> <p> <code>IgnoredUID</code> - (Required) The user ID (UID) of the proxy container as defined by the <code>user</code> parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If <code>IgnoredGID</code> is specified, this field can be empty.</p> </li> <li> <p> <code>IgnoredGID</code> - (Required) The group ID (GID) of the proxy container as defined by the <code>user</code> parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If <code>IgnoredUID</code> is specified, this field can be empty.</p> </li> <li> <p> <code>AppPorts</code> - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the <code>ProxyIngressPort</code> and <code>ProxyEgressPort</code>.</p> </li> <li> <p> <code>ProxyIngressPort</code> - (Required) Specifies the port that incoming traffic to the <code>AppPorts</code> is directed to.</p> </li> <li> <p> <code>ProxyEgressPort</code> - (Required) Specifies the port that outgoing traffic from the <code>AppPorts</code> is directed to.</p> </li> <li> <p> <code>EgressIgnoredPorts</code> - (Required) The egress traffic going to the specified ports is ignored and not redirected to the <code>ProxyEgressPort</code>. It can be an empty list.</p> </li> <li> <p> <code>EgressIgnoredIPs</code> - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the <code>ProxyEgressPort</code>. It can be an empty list.</p> </li> </ul>"""
