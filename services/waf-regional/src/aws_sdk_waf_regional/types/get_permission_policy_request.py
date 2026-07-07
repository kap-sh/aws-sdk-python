"""Generated from Smithy shape ``com.amazonaws.wafregional#GetPermissionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_arn


class GetPermissionPolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_waf_regional.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the RuleGroup for which you want to get the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPermissionPolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPermissionPolicyRequest:
    out: GetPermissionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("GetPermissionPolicyRequest.resource_arn required")
    return out
