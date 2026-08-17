"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchNetworkPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.open_search_policy_name
    import capo_cloudwatch_logs.types.open_search_resource_status


class OpenSearchNetworkPolicy(TypedDict, closed=True):
    policy_name: NotRequired[
        "capo_cloudwatch_logs.types.open_search_policy_name.OpenSearchPolicyName"
    ]
    """<p>The name of the network policy.</p>"""
    status: NotRequired[
        "capo_cloudwatch_logs.types.open_search_resource_status.OpenSearchResourceStatus"
    ]
    """<p>This structure contains information about the status of this OpenSearch Service resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchNetworkPolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "status" in value:
        import capo_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            capo_cloudwatch_logs.types.open_search_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchNetworkPolicy:
    out: OpenSearchNetworkPolicy = {}  # type: ignore[typeddict-item]
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    if data.get("status") is not None:
        import capo_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            capo_cloudwatch_logs.types.open_search_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
