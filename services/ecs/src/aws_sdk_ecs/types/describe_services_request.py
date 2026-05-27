"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServicesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_field_list
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class DescribeServicesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the service or services you are describing were launched in any cluster other than the default cluster.</p>"""
    services: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A list of services to describe. You may specify up to 10 services to describe in a single operation.</p>"""
    include: NotRequired["aws_sdk_ecs.types.service_field_list.ServiceFieldList"]
    """<p>Determines whether you want to see the resource tags for the service. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""
