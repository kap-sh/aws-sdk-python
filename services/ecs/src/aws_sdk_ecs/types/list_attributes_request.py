"""Generated from Smithy shape ``com.amazonaws.ecs#ListAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.target_type


class ListAttributesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.</p>"""
    target_type: "aws_sdk_ecs.types.target_type.TargetType"
    """<p>The type of the target to list attributes with.</p>"""
    attribute_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the attribute to filter the results with. </p>"""
    attribute_value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The value of the attribute to filter results with. You must also specify an attribute name to use this parameter.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListAttributes</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of cluster results that <code>ListAttributes</code> returned in paginated output. When this parameter is used, <code>ListAttributes</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListAttributes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListAttributes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
