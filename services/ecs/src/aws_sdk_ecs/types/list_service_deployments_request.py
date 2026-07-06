"""Generated from Smithy shape ``com.amazonaws.ecs#ListServiceDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.created_at
    import aws_sdk_ecs.types.service_deployment_status_list
    import aws_sdk_ecs.types.string


class ListServiceDeploymentsRequest(TypedDict, closed=True):
    service: "aws_sdk_ecs.types.string.String"
    """<p>The ARN or name of the service</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The cluster that hosts the service. This can either be the cluster name or ARN. Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. If you don't specify a cluster, <code>default</code> is used.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.service_deployment_status_list.ServiceDeploymentStatusList"
    ]
    """<p>An optional filter you can use to narrow the results. If you do not specify a status, then all status values are included in the result.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.created_at.CreatedAt"]
    """<p>An optional filter you can use to narrow the results by the service creation date. If you do not specify a value, the result includes all services created before the current time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListServiceDeployments</code> request indicating that more results are available to fulfill the request and further calls are needed. If you provided <code>maxResults</code>, it's possible the number of results is fewer than <code>maxResults</code>.</p>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of service deployment results that <code>ListServiceDeployments</code> returned in paginated output. When this parameter is used, <code>ListServiceDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServiceDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServiceDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceDeploymentsRequest) -> dict:
    out: dict = {}
    out["service"] = value["service"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "status" in value:
        import aws_sdk_ecs.types.service_deployment_status_list

        out["status"] = (
            aws_sdk_ecs.types.service_deployment_status_list.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created_at" in value:
        import aws_sdk_ecs.types.created_at

        out["createdAt"] = aws_sdk_ecs.types.created_at.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceDeploymentsRequest:
    out: ListServiceDeploymentsRequest = {}  # type: ignore[typeddict-item]
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError("ListServiceDeploymentsRequest.service required")
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "status" in data:
        import aws_sdk_ecs.types.service_deployment_status_list

        out["status"] = (
            aws_sdk_ecs.types.service_deployment_status_list.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_ecs.types.created_at

        out["created_at"] = aws_sdk_ecs.types.created_at.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
