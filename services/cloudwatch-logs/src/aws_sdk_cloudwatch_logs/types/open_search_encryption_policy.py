"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchEncryptionPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.open_search_policy_name
    import aws_sdk_cloudwatch_logs.types.open_search_resource_status


class OpenSearchEncryptionPolicy(TypedDict):
    policy_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_policy_name.OpenSearchPolicyName"
    ]
    """<p>The name of the encryption policy.</p>"""
    status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_resource_status.OpenSearchResourceStatus"
    ]
    """<p>This structure contains information about the status of this OpenSearch Service resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchEncryptionPolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "status" in value:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchEncryptionPolicy:
    out: OpenSearchEncryptionPolicy = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
