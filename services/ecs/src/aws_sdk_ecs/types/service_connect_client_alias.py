"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectClientAlias``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.port_number
    import aws_sdk_ecs.types.service_connect_test_traffic_rules
    import aws_sdk_ecs.types.string


class ServiceConnectClientAlias(TypedDict):
    port: "aws_sdk_ecs.types.port_number.PortNumber"
    """<p>The listening port number for the Service Connect proxy. This port is available inside of all of the tasks within the same namespace.</p> <p>To avoid changing your applications in client Amazon ECS services, set this to the same port that the client application uses by default. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html\">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    dns_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>dnsName</code> is the name that you use in the applications of client tasks to connect to this service. The name must be a valid DNS name but doesn't need to be fully-qualified. The name can include up to 127 characters. The name can include lowercase letters, numbers, underscores (_), hyphens (-), and periods (.). The name can't start with a hyphen.</p> <p>If this parameter isn't specified, the default value of <code>discoveryName.namespace</code> is used. If the <code>discoveryName</code> isn't specified, the port mapping name from the task definition is used in <code>portName.namespace</code>.</p> <p>To avoid changing your applications in client Amazon ECS services, set this to the same name that the client application uses by default. For example, a few common names are <code>database</code>, <code>db</code>, or the lowercase name of a database, such as <code>mysql</code> or <code>redis</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html\">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    test_traffic_rules: NotRequired[
        "aws_sdk_ecs.types.service_connect_test_traffic_rules.ServiceConnectTestTrafficRules"
    ]
    """<p>The configuration for test traffic routing rules used during blue/green deployments with Amazon ECS Service Connect. This allows you to route a portion of traffic to the new service revision of your service for testing before shifting all production traffic.</p>"""
