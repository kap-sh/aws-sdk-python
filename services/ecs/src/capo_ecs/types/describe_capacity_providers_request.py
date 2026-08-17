"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeCapacityProvidersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_field_list
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class DescribeCapacityProvidersRequest(TypedDict, closed=True):
    capacity_providers: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The short name or full Amazon Resource Name (ARN) of one or more capacity providers. Up to <code>100</code> capacity providers can be described in an action.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the cluster to describe capacity providers for. When specified, only capacity providers associated with this cluster are returned, including Amazon ECS Managed Instances capacity providers.</p>"""
    include: NotRequired[
        "capo_ecs.types.capacity_provider_field_list.CapacityProviderFieldList"
    ]
    """<p>Specifies whether or not you want to see the resource tags for the capacity provider. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of account setting results returned by <code>DescribeCapacityProviders</code> in paginated output. When this parameter is used, <code>DescribeCapacityProviders</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeCapacityProviders</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 10. If this parameter is not used, then <code>DescribeCapacityProviders</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeCapacityProviders</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCapacityProvidersRequest) -> dict:
    out: dict = {}
    if "capacity_providers" in value:
        import capo_ecs.types.string_list

        out["capacityProviders"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["capacity_providers"]
        )
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "include" in value:
        import capo_ecs.types.capacity_provider_field_list

        out["include"] = (
            capo_ecs.types.capacity_provider_field_list.serialize_aws_json_1_1(
                value["include"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCapacityProvidersRequest:
    out: DescribeCapacityProvidersRequest = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviders") is not None:
        import capo_ecs.types.string_list

        out["capacity_providers"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["capacityProviders"]
        )
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("include") is not None:
        import capo_ecs.types.capacity_provider_field_list

        out["include"] = (
            capo_ecs.types.capacity_provider_field_list.deserialize_aws_json_1_1(
                data["include"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
