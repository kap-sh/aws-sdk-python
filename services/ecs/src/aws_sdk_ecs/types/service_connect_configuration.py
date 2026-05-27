"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.log_configuration
    import aws_sdk_ecs.types.service_connect_access_log_configuration
    import aws_sdk_ecs.types.service_connect_service_list
    import aws_sdk_ecs.types.string


class ServiceConnectConfiguration(TypedDict):
    enabled: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Specifies whether to use Service Connect with this service.</p>"""
    namespace: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace for use with Service Connect. The namespace must be in the same Amazon Web Services Region as the Amazon ECS service and cluster. The type of namespace doesn't affect Service Connect. For more information about Cloud Map, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html\">Working with Services</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    services: NotRequired[
        "aws_sdk_ecs.types.service_connect_service_list.ServiceConnectServiceList"
    ]
    """<p>The list of Service Connect service objects. These are names and aliases (also known as endpoints) that are used by other Amazon ECS services to connect to this service. </p> <p>This field is not required for a \"client\" Amazon ECS service that's a member of a namespace only to connect to other services within the namespace. An example of this would be a frontend application that accepts incoming requests from either a load balancer that's attached to the service or by other means.</p> <p>An object selects a port from the task definition, assigns a name for the Cloud Map service, and a list of aliases (endpoints) and ports for client applications to refer to this service.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_ecs.types.log_configuration.LogConfiguration"
    ]
    access_log_configuration: NotRequired[
        "aws_sdk_ecs.types.service_connect_access_log_configuration.ServiceConnectAccessLogConfiguration"
    ]
    """<p>The configuration for Service Connect access logging. Access logs capture detailed information about requests made to your service, including request patterns, response codes, and timing data. They can be useful for debugging connectivity issues, monitoring service performance, and auditing service-to-service communication for security and compliance purposes.</p> <note> <p>To enable access logs, you must also specify a <code>logConfiguration</code> in the <code>serviceConnectConfiguration</code>.</p> </note>"""
