"""Generated from Smithy shape ``com.amazonaws.ecs#PutAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes
    import aws_sdk_ecs.types.string


class PutAttributesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.</p>"""
    attributes: "aws_sdk_ecs.types.attributes.Attributes"
    """<p>The attributes to apply to your resource. You can specify up to 10 custom attributes for each resource. You can specify up to 10 attributes in a single call.</p>"""
