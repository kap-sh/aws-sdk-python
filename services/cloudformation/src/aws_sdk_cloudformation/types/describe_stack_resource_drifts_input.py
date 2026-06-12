"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackResourceDriftsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.boxed_max_results
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_name_or_id
    import aws_sdk_cloudformation.types.stack_resource_drift_status_filters


class DescribeStackResourceDriftsInput(TypedDict):
    stack_name: NotRequired[
        "aws_sdk_cloudformation.types.stack_name_or_id.StackNameOrId"
    ]
    """<p>The name of the stack for which you want drift information.</p>"""
    stack_resource_drift_status_filters: NotRequired[
        "aws_sdk_cloudformation.types.stack_resource_drift_status_filters.StackResourceDriftStatusFilters"
    ]
    """<p>The resource drift status values to use as filters for the resource drift results returned.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration in that the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected template values.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation doesn't currently return this value.</p> </li> <li> <p> <code>UNKNOWN</code>: CloudFormation could not run drift detection for the resource.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "aws_sdk_cloudformation.types.boxed_max_results.BoxedMaxResults"
    ]
    """<p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackResourceDriftsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "stack_resource_drift_status_filters" in value:
        import aws_sdk_cloudformation.types.stack_resource_drift_status_filters

        aws_sdk_cloudformation.types.stack_resource_drift_status_filters.serialize_query(
            value["stack_resource_drift_status_filters"],
            pairs,
            f"{prefix}.StackResourceDriftStatusFilters",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> DescribeStackResourceDriftsInput:
    out: DescribeStackResourceDriftsInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_stack_resource_drift_status_filters = el.find(
        "StackResourceDriftStatusFilters"
    )
    if child_stack_resource_drift_status_filters is not None:
        import aws_sdk_cloudformation.types.stack_resource_drift_status_filters

        out["stack_resource_drift_status_filters"] = (
            aws_sdk_cloudformation.types.stack_resource_drift_status_filters.deserialize_query(
                child_stack_resource_drift_status_filters
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
