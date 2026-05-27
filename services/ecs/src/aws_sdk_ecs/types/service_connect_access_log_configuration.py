"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectAccessLogConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_connect_access_logging_format
    import aws_sdk_ecs.types.service_connect_include_query_parameters


class ServiceConnectAccessLogConfiguration(TypedDict):
    format: "aws_sdk_ecs.types.service_connect_access_logging_format.ServiceConnectAccessLoggingFormat"
    """<p>The format for Service Connect access log output. Choose TEXT for human-readable logs or JSON for structured data that integrates well with log analysis tools.</p>"""
    include_query_parameters: NotRequired[
        "aws_sdk_ecs.types.service_connect_include_query_parameters.ServiceConnectIncludeQueryParameters"
    ]
    """<p>Specifies whether to include query parameters in Service Connect access logs.</p> <p>When enabled, query parameters from HTTP requests are included in the access logs. Consider security and privacy implications when enabling this feature, as query parameters may contain sensitive information such as request IDs and tokens. By default, this parameter is <code>DISABLED</code>.</p>"""
