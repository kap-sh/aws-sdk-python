"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListDaemonsRequest(TypedDict):
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster to filter daemons by. If not specified, daemons from all clusters are returned.</p>"""
    capacity_provider_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The Amazon Resource Names (ARNs) of the capacity providers to filter daemons by. Only daemons associated with the specified capacity providers are returned.</p>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of daemon results that <code>ListDaemons</code> returned in paginated output. When this parameter is used, <code>ListDaemons</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemons</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemons</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListDaemons</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
