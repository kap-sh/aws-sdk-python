"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class ListDaemonsRequest(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster to filter daemons by. If you do not specify a cluster, the default cluster is assumed.</p>"""
    capacity_provider_arns: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The Amazon Resource Names (ARNs) of the capacity providers to filter daemons by. Only daemons associated with the specified capacity providers are returned.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of daemon results that <code>ListDaemons</code> returned in paginated output. When this parameter is used, <code>ListDaemons</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemons</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemons</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListDaemons</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDaemonsRequest) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "capacity_provider_arns" in value:
        import capo_ecs.types.string_list

        out["capacityProviderArns"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["capacity_provider_arns"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDaemonsRequest:
    out: ListDaemonsRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("capacityProviderArns") is not None:
        import capo_ecs.types.string_list

        out["capacity_provider_arns"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["capacityProviderArns"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
